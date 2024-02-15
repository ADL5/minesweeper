# minesweeper
its my beta minesweeper game.

Hidden feature.
If you click on the emoticon with your right mouse button, a window will open in which you can enable/disable the recursive akkord function(default=False,u need to update value every session, because iam lazy) and view your record in each discipline.
akkord - if when you click on a number around it the number of flags is equal to the value of the number, then all cells where there are no flags will open.
A recursive chord is a chord that extends to adjacent numbers.
to swap field size, found values n and m in code

Rules.
The flat playing field is divided into adjacent cells (squares), some of which are “mined”; the number of “mined” cells is known. The goal of the game is to open all cells that do not contain mines.
The player opens the cells, being careful not to open a cell with a mine. Having opened a cell with a mine, he loses. The mines are placed after the first turn, so it is impossible to lose on the first turn. If there is no mine under an open cell, then a number appears in it showing how many cells adjacent to the one just opened are “mined”; Using these numbers, the player tries to calculate the location of the mines, but sometimes even in the middle and at the end of the game, some cells still have to be opened at random. If there are also no mines under the adjacent cells, then some “non-mined” area opens up to the cells that have numbers. The player can mark “mined” cells so as not to accidentally open them. By opening all the “unmined” cells, the player wins.
