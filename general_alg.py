from PIL import Image
import os, sys, random, shutil

# my stuff
movie = False
tmps = True
size = 10,10
frames = 500
pics = 1
color = [  (0,0,0),	(100,0,0),	(200,0,0),	(250,0,0),
		(250,100,0),	(250,200,0),	(250,250,0),	(250,250,100),
		(250,250,200),	(250,250,250),	(200,250,250),	(100,250,250),
		(0,250,250),	(0,200,250),	(0,100,250),	(0,0,250),
		(0,0,200),	(0,0,100),	(0,100,0),	(0,200,0)]

#standard variables
r = 2 # range
t = 11 # threshold
c = 3 # modes
n = 'M' # N or M (Von Neumann or Moore)




def print_help():
	print 'arguements are as follows'
	print '  -r=<range>       # r gives you the neighboorhood range'
	print '  -t=<threshold>   # t gives you the number of passed cells in the range'
	print '  -c=<Modes>       # c gives you number of modes for celss'
	print '  -n=<Range Method># n gives you the neighborhood range method'
	print '      -M is extended moore (1 range is 1 of (N,S,E,W,NW,NE,SW,SE))'
	print '      -N is Von Neumann (1 range is 1 of (N,S,E,W))'
	#print '      -G is GH (not implemented yet)'
	sys.exit()

for u in xrange(pics):
	print u
	# setup with random initiliazation
	color = []
	for a in xrange(c):
		color.append((random.randint(0,255),random.randint(0,255),random.randint(0,255))) 

	o_l = []
	for x in xrange(size[0]):
		o_line = []
		for y in xrange(size[1]):
			o_line.append(random.randint(0,c-1))
		o_l.append(o_line)
	# build frames
	if os.path.isdir('tmp'):
		shutil.rmtree('tmp')
	os.mkdir('tmp')
	for count in xrange(frames):
		#build next frame
		n_l = []
		for x in xrange(size[0]):
			n_line = []
			for y in xrange(size[1]):
				val = (o_l[x][y] + 1)%c
				val_count = 0
				if n == 'M':
					for a in xrange(-r,r+1):
						for b in xrange(-r,r+1):
							if val == o_l[(x+a)%size[0]][(y+b)%size[1]]:
								val_count += 1
				elif n == 'N':
					for a in xrange(-r,r+1):
						for b in xrange(-r,r+1):
							if abs(a) + abs(b) <= r:
								if val == o_l[(x+a)%size[0]][(y+b)%size[1]]:
									val_count += 1
				else:
					print "Im Mad"
					sys.exit()
				if val_count >= t:
					n_line.append(val)
				else:
					n_line.append(o_l[x][y])
			n_l.append(n_line)
		o_l = n_l
		#make new image frame
		if tmps:
			im = Image.new('RGB',(size[0],size[1]))
			pix = im.load()
			for x in xrange(size[0]):
				for y in xrange(size[1]):
					pix[x,y] = color[o_l[x][y]]
			
			im.save('tmp/img' + (5-len(str(count)))*'0' + str(count) + '.png')
	im = Image.new('RGB',(size[0],size[1]))
	pix = im.load()
	for x in xrange(size[0]):
		for y in xrange(size[1]):
			pix[x,y] = color[o_l[x][y]]
	im.save('output/' + chr(random.randint(65,90)) + chr(random.randint(65,90)) + chr(random.randint(65,90)) + chr(random.randint(65,90)) + chr(random.randint(65,90)) + '.png')
	if movie and tmps:
		os.system('avconv -f image2 -i tmp/img%05d.png -y out.mp4')
