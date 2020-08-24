import math
import copy

# Declaration of example sudoku board
Board = [   [2, 0, 0, 0, 3, 1, 0, 0, 6],
            [5, 0, 7, 4, 0, 8, 2, 3, 9],
            [0, 6, 0, 0, 0, 0, 4, 0, 7],

            [3, 4, 0, 2, 5, 0, 0, 0, 0],
            [0, 8, 1, 0, 0, 0, 6, 2, 5],
            [6, 5, 0, 0, 0, 7, 0, 4, 0],

            [9, 2, 0, 1, 7, 3, 0, 6, 4],
            [1, 0, 5, 6, 8, 0, 7, 0, 2],
            [4, 7, 0, 0, 2, 5, 3, 0, 0]]

# BoardSolved can be used to check if the program is working properly
BoardSolved = [ [2, 9, 4, 7, 3, 1, 8, 5, 6],
                [5, 1, 7, 4, 6, 8, 2, 3, 9],
                [8, 6, 3, 5, 9, 2, 4, 1, 7],

                [3, 4, 9, 2, 5, 6, 1, 7, 8],
                [7, 8, 1, 3, 4, 9, 6, 2, 5],
                [6, 5, 2, 8, 1, 7, 9, 4, 3],

                [9, 2, 8, 1, 7, 3, 5, 6, 4],
                [1, 3, 5, 6, 8, 4, 7, 9, 2],
                [4, 7, 6, 9, 2, 5, 3, 8, 1]]

# Prints a Board in a ASCII fashion
def printBoard(mtx = Board):
    asciiBoard = ''
    for line in mtx:
        asciiBoard += '[ '
        for digit in line:
            asciiBoard += str(digit) + ' '

        asciiBoard += ']\n'

    print(asciiBoard)
    

# Returns vertical columns of numbers extracted from matrix
def returnCols(matrix):
    output = []

    for loop in range(9):
        newCol = []
        for line in matrix:
            newCol.append(line[loop])

        output.append(newCol)

    #print('Cols:\n' + str(output))

    return output

# Returns a list of lists representing 3x3 quads. This is not needed but I feel like it will make the process much more readable
def returnQuads(matrix):
    output =   [[],[],[],
                [],[],[],
                [],[],[]]

    for col in range(9):
        for row in range(9):
            if col < 3:
                if row < 3:
                    output[0].append(matrix[col][row])
                if row < 6 and row >= 3:
                    output[1].append(matrix[col][row])
                if row < 9 and row >=6:
                    output[2].append(matrix[col][row])

            if col < 6 and col >=3:
                if row < 3:
                    output[3].append(matrix[col][row])
                if row < 6 and row >=3:
                    output[4].append(matrix[col][row])
                if row < 9 and row >=6:
                    output[5].append(matrix[col][row])

            if col < 9 and col >=6:
                if row < 3:
                    output[6].append(matrix[col][row])
                if row < 6 and row >=3:
                    output[7].append(matrix[col][row])
                if row < 9 and row >=6:
                    output[8].append(matrix[col][row])

    #print('Quads:\n' + str(output))
    return output 
             

# Class that transforms a board into something that is easier to operate on. Also more intuitive and clearer to read
class Sudoku:
    def __init__(self, matrix):
        self.rows = matrix
        self.cols = returnCols(matrix)
        self.quads = returnQuads(matrix)
        self.solved = False

        #self.pretendents = 

    # In case we need to assign new (maybe slightly transformed) matrix
    def redefine(self, matrix):
        self.rows = matrix
        self.cols = returnCols(matrix)
        self.quads = returnQuads(matrix)

    def isSolved(self):
        for row in self.rows:
            for cell in row:
                if cell == 0:
                    return False

        return True

    # Prints the board in ASCII fashion
    def printBoard(self):
        asciiBoard = ''
        for line in self.rows:
            asciiBoard += '[ '
            for digit in line:
                asciiBoard += str(digit) + ' '

            asciiBoard += ']\n'

        print(asciiBoard)

    # Changes value in given row and col
    def changeValue(self, row:int, col:int, newValue:int):
        hero = copy.deepcopy(self.rows)
        hero[row][col] = newValue
        self.redefine(hero)

    # Checks whether the digit checks the sudoku rules
    def isDigitValid(self, row, col, digit):
        debug = False
        if digit in self.rows[row]:                                         # is present in row
            if debug == True: print('Not valid due to ROW overpopulation')
            return False
        if digit in self.cols[col]:                                         # is present in column
            if debug == True: print('Not valid due to COLUMN overpopulation')
            return False
        if digit in self.quads[returnQuadIndex(row, col)]:      # is present in quad
            if debug == True: print('Not valid due to QUAD overpopulation')
            return False

        if debug == True: print('row: {0} col: {1}    valid: {2}'.format(row, col, True))
        # If not returned earlier then valid
        return True

# Creates a list of lists containing pretendents for a valid digit for a chosen Sudoku object
def fillPretendents(original: Sudoku):
    
    output = []
    for row in range(9):
        for col in range(9):
            newInsert = []
            # insert here if statement that check if there was blank space
            if original.rows[row][col] == 0:
                for digit in range(1,10):
                    if original.isDigitValid(row, col, digit):
                        newInsert.append(digit)

            if len(newInsert) == 1:
                original.changeValue(row, col, newInsert[0])

            output.append(newInsert)

    #print(output)

def returnQuadIndex(row:int, col:int):
    if row < 3:
        if col < 3:
            return 0
        if col < 6 and col >= 3:
            return 1
        if col < 9 and col >= 6:
            return 2

    if row < 6 and row >= 3:
        if col < 3:
            return 3
        if col < 6 and col >= 3:
            return 4
        if col < 9 and col >= 6:
            return 5

    if row < 9 and row >= 6:
        if col < 3:
            return 6
        if col < 6 and col >= 3:
            return 7
        if col < 9 and col >= 6:
            return 8
