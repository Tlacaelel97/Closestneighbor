# Closest Neighbour

## Resume
The algorithm works by iterating through the list of points and finding the closest neighbour to each point. The distance between two points is calculated using Euclidean

## Usage
Have the function ClosestNeighbour(strArr) read the matrix of numbers stored in strArr which
will be a 2D matrix that contains only the integers 1, 0, or 2.
Then from the position in the matrix where a 1 is, return the number of spaces either left,
right, down, or up you must move to reach an enemy which is represented by a 2.
You are able to wrap around one side of the matrix to the other as well.

For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following:

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from
the 1 by moving left to wrap to the other side and then moving down once.
The array can contain any number of 0's and 2's, but only a single 1.
It may not contain any 2's at all as well, where in that case your program should return a 0.

The program should also return 0 if the matrix is malformed, meaning the column count is not the
same in all rows.

The program use the example above by defect to execute, just press enter to doi it. 
The user can introduce any matrix by typing it, then press enter.

## Author
![Tlacaelel Flores](https://github.com/Tlacaelel97)