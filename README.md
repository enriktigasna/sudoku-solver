# Sudoku solver in python

I was sick for a few days, and when I got back I needed to brush up on algorithms and maybe some graph theory so I made this after watching [Introduction to Graph Theory](https://www.youtube.com/watch?v=LFKZLXVO-Dg)

First I generate an adjacency list so that each square has an edge to every other square that it shouldn't have an equal number in
Eg: all squares down, to the side and in it's own square.

I created a function to find what you can put in a square at some given coordinates without breaking the rules. And another one to return the easiest coordinates to solve (the ones with the least possible numbers to put in the square)

Every time there is more than one possibility in the easiest-to-solve square, I add the other possibilities to the stack, so that incase I pick the wrong possibility and it ends up being unsolvable, I can backtrack to the correct one, and continue from there.

## Examples
![image](https://github.com/enriktigasna/sudoku-solver/assets/42349218/3f508bd1-4682-4c5e-9bd6-b1f4ad3c4297)
![image](https://github.com/enriktigasna/sudoku-solver/assets/42349218/304732e4-784c-45e9-9da8-741c4df00bc6)
