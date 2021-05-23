# -*- coding: utf-8 -*-
"""
Created on Sat May  8 00:18:27 2021

@author: tlaca
"""
"""
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
"""

"""The program use the example above by defect to execute. The user can intruduce any matrix by typing in the 
variable Starr"""

#%% def of the function      
def ClosestNeighbour(strArr):
    
    #variables
    flagg =0
    r = strArr[0].split() #first row of the matrix
    check = len(r[0]) #lenght of the first row of the matrix
    character = 0 #number of characters
    
    #check that the matrix is malformed or not 
    for i in range(0,len(strArr)):
        cosi = strArr[i].split()
        if check == len(cosi[0]):
            flagg += 1
    #if the matrix is malformed print 0, otherwise, continue   
    if flagg != len(strArr):
        print('0, matrix malformed')
    elif flagg == len(strArr): 
        #identify the position of the character and the enemies
        enemies = []
        for i,row in list(enumerate(strArr)):
            for j, col in enumerate(row):
                if col == '1':
                    px, py = (i,j)
                    character += 1
                if col == '2':
                    enemies.append((i,j))
        # if there is no enemies, return 0
        if len(enemies) == 0:
            print('The number of spaces you must move to reach an enemy is: ',0)
        #if there is only one character, Calculate the distance to every enemy in the matrix and save it in the moves list
        if character == 1: 
            moves = []
            for x, y in enemies:
                no_wrap = abs(px-x) + abs(py-y)
                col_wrap, row_wrap = abs(px-x) + abs(py-(y-len(strArr))), abs(px-(x-len(strArr))) + abs(py-y)
                moves.append(min(no_wrap, col_wrap, row_wrap))
            
            print('The number of spaces you must move to reach an enemy is: ',min(moves))
        else: #if there are 2 or more character (or annother case), print an error
            print('ERROR. The program must contain one character')
    return None
            


#%%Test of the program

#-----------------------------------------------------------------
#---------------Introduce the list that you prefer----------------
#-----------------------------------------------------------------
strArr=["0000","1000","0002","0002",]   
ClosestNeighbour(strArr)


# %%
