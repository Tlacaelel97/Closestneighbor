# -*- coding: utf-8 -*-


# %% def of the function
def ClosestNeighbour(strArr):
    # variables
    flagg = 0
    r = strArr[0].split()  # first row of the matrix
    check = len(r[0])  # lenght of the first row of the matrix
    character = 0  # number of characters

    # check that the matrix is malformed or not
    for i in range(0, len(strArr)):
        cosi = strArr[i].split()
        if check == len(cosi[0]):
            flagg += 1
    # if the matrix is malformed print 0, otherwise, continue
    if flagg != len(strArr):
        print("0, matrix malformed")
    elif flagg == len(strArr):
        # identify the position of the character and the enemies
        enemies = []
        for i, row in list(enumerate(strArr)):
            for j, col in enumerate(row):
                if col == "1":
                    px, py = (i, j)
                    character += 1
                if col == "2":
                    enemies.append((i, j))
        # if there is no enemies, return 0
        if len(enemies) == 0:
            print("The number of spaces you must move to reach an enemy is: ", 0)
        # if there is only one character, Calculate the distance to every enemy in the matrix and save it in the moves list
        if character == 1:
            moves = []
            for x, y in enemies:
                no_wrap = abs(px - x) + abs(py - y)
                col_wrap, row_wrap = abs(px - x) + abs(py - (y - len(strArr))), abs(
                    px - (x - len(strArr))
                ) + abs(py - y)
                moves.append(min(no_wrap, col_wrap, row_wrap))

            print(
                "The number of spaces you must move to reach an enemy is: ", min(moves)
            )
        else:  # if there are 2 or more character (or annother case), print an error
            print("ERROR. The program must contain one character")
    return None


# %%Test of the program
if __name__ == "__main__":
    # -----------------------------------------------------------------
    # ---------------Introduce the list that you prefer----------------
    # -----------------------------------------------------------------
    # Input data
    input_data = input(
        "Type the numbers of the array, like the next example:\n\n0000\n1000\n0002\n0002\n\n Press enter to use the example from above.\n"
    )
    # Create the array
    strArr = [input_data]
    # The lenght depends on the number of spaces used, to make a square matrix
    for i in range(len(input_data) - 1):
        strArr.append(input())
    # Set the default example
    if input_data == "":
        strArr = [
            "0000",
            "1000",
            "0002",
            "0002",
        ]
    ClosestNeighbour(strArr)
