GCA
===

Goal
----
This is just a freetime project, but my goal is to find my own rules set that exhibits interesting and unique qualities from other automata
Dependencies
------------
this program is dependent on Python 2.7(I use .5 but im sure you can use whatever PIL is ok with), PIL, and whatever video encoder you want to use(right now its avconv).
General Cellular Automata
-------------------------
This set of programs allow you to simulate cellular automatas. I will be expanding on the number of supported automatas as the project evolves. Right now, you can simulate CCA (cyclical cellular automata).
You can also make videos from the program. I used ffmpeg for the windows version, and avconv for the linux version, you can change yours to fit your needs.
Improvements to be made
-----------------------
1. I was going to use this program as an introduction to gpu programming as the cells each have shared memory of the other cells. As of right now though, it does not use anything. I will probably be using PyCUDA at some point in the future if you want to help me learn it.

2. I need to add some different types of valuing algorithms, right now it is an advancing alogithm (if passed mode = (mode + 1)%modes) but some different ones can be applied. In general though, the advancing algorithm can give you a good idea of what is supposed to happen

Feel free to add things to this list.
