#student name: Zhi Chuen Tan
#student number: 65408361

def checkColumn(puzzle: list, column: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param column: the column to check (a value between 0 to 8)

        This function checks the indicated column of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    columnVals: list = [' '] * 9    # initial value assignment
    checkSum: int = 1               # checkSum assumes all numbers are in the column unless shown otherwise

    # stores each value in a given column in a list
    for i in range(9):
        columnVals[i] = puzzle[i][column]
    
    # checks if each number (1-9) is present in the list
    for j in range (1,10):
        if j not in columnVals:
            checkSum *= 0 # if a value is not present, checkSum will be set to 0 permanently, as anything*0=0
    
    # if checkSum is 0, that means at least one number (1-9) is not present in the column
    if checkSum == 0:
        print("Column " + str(column) + " not valid")
    
    # if checkSum is 1, that means all numbers (1-9) are present in the column
    elif checkSum == 1:
        print("Column " + str(column) + " valid")

    # sanity check-point, should never end up here, used for debugging logic    
    else:
        print("ERROR: SHOULDN'T END UP HERE")

def checkRow(puzzle: list, row: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param row: the row to check (a value between 0 to 8)

        This function checks the indicated row of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    checkSum: int = 1        # checkSum first assumes all numbers are in the row

    # checks if each number (1-9) is present in the row
    for i in range (1,10):
        if i not in puzzle[row]:
            checkSum *= 0   # if a value is not present, checkSum will be set to 0 permanently, as anything*0=0
    
    # if checkSum is 0, that means at least one number (1-9) is not present in the row
    if checkSum == 0:
        print("Row " + str(row) + " not valid")
    
    # if checkSum is 1, that means all numbers (1-9) are present in the row
    elif checkSum == 1:
        print("Row " + str(row) + " valid")

    # sanity check-point, should never end up here, used for debugging logic    
    else:
        print("ERROR: SHOULDN'T END UP HERE")

def checkSubgrid(puzzle: list, subgrid: int):
    """ 
        param puzzle: a list of lists containing the puzzle 
        param subgrid: the subgrid to check (a value between 0 to 8)
        Subgrid numbering order:    0 1 2
                                    3 4 5
                                    6 7 8
        where each subgrid itself is a 3x3 portion of the original list
        
        This function checks the indicated subgrid of the puzzle, and 
        prints whether it is valid or not. 
        
        As usual, this function must not mutate puzzle 
    """
    subGridVals: list = [' '] * 9       # initial value assignment
    checkSum: int = 1                   # checkSum assumes all numbers are in the column unless shown otherwise
    index: int = 0

    # checks cases for each individual subgrid
    if subgrid == 0:
        for i in range(0, 3):       # subgrid 0 is rows 0-2...
            for j in range(0, 3):   # ... and columns 0-2
                subGridVals[index] = puzzle[i][j]
                index += 1          # iterating index for the list
    
    elif subgrid == 1:
        for i in range(0, 3):       # subgrid 1 is rows 0-2...
            for j in range(3, 6):   # ... and columns 3-5
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 2:
        for i in range(0, 3):       # subgrid 2 is rows 0-2...
            for j in range(6, 9):   # ... and columns 6-8
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 3:
        for i in range(3, 6):       # subgrid 3 is rows 3-5...
            for j in range(0, 3):   # ... and columns 0-2
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 4:
        for i in range(3, 6):       # subgrid 4 is rows 3-5...
            for j in range(3, 6):   # ... and column 3-5
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 5:
        for i in range(3, 6):       # subgrid 5 is rows 3-5...
            for j in range(6, 9):   # ... and column 6-8
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 6:
        for i in range(6, 9):       # subgrid 6 is rows 6-8...
            for j in range(0, 3):   # ... and column 0-2
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 7:
        for i in range(6, 9):       # subgrid 7 is rows 6-8...
            for j in range(3, 6):   # ... and columns 3-5
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    elif subgrid == 8:
        for i in range(6, 9):       # subgrid 8 is rows 6-8...
            for j in range(6, 9):   # ... and columns 6-8
                subGridVals[index] = puzzle[i][j]
                index += 1
    
    else:
        print ("ERROR: SHOULDN'T END UP HERE (subGridVals)")  #

    # checks if each number (1-9) is present in the subgrid
    for i in range (1,10):
        if i not in subGridVals:
            checkSum *= 0 # if a value is not present, checkSum will be set to 0 permanently, as anything*0=0
    
    # if checkSum is 0, that means at least one number (1-9) is not present in the subgrid
    if checkSum == 0:
        print("Subgrid " + str(subgrid) + " not valid")
    
    # if checkSum is 1, that means all numbers (1-9) are present in the subgrid
    elif checkSum == 1:
        print("Subgrid " + str(subgrid) + " valid")

    # sanity check-point, should never end up here, used for debugging logic    
    else:
        print("ERROR: SHOULDN'T END UP HERE (subgrid valid)")


if __name__ == "__main__":
    test1 = [ [6, 2, 4, 5, 3, 9, 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5],
              [1, 4, 3, 8, 6, 5, 7, 2, 9],
              [9, 5, 8, 2, 4, 7, 3, 6, 1],
              [7, 6, 2, 3, 9, 1, 4, 5, 8],
              [3, 7, 1, 9, 5, 6, 8, 4, 2],
              [4, 9, 6, 1, 8, 2, 5, 7, 3],
              [2, 8, 5, 4, 7, 3, 9, 1, 6]
            ]
    test2 = [ [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 3, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ],
              [6, 2, 4, 5, 3, 9 , 1, 8, 7],
              [5, 1, 9, 7, 2, 8, 6, 3, 4],
              [8, 3, 7, 6, 1, 4, 2, 9, 5 ]
            ]
    
    testcase = test2   #modify here for other testcases
    SIZE = 9

    for col in range(SIZE):  #checking all columns
        checkColumn(testcase, col)
    for row in range(SIZE):  #checking all rows
        checkRow(testcase, row)
    for subgrid in range(SIZE):   #checking all subgrids
        checkSubgrid(testcase, subgrid)