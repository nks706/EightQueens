import random

queenPosition = [-99,-99,-99,-99,-99,-99,-99,-99]

def intialize(board):
    for i in range (0,8):
        lowestConflictValue = 100
        lowestConflictPositions = []

        for j in range (0,8):
            currentConflictValue = findConflicts(board,i,j)
            
            if (currentConflictValue < lowestConflictValue):
                lowestConflictValue = currentConflictValue
                #lowestConflictPositions.clear()
                del lowestConflictPositions[:]
                lowestConflictPositions.append(j)
                
            elif (currentConflictValue == lowestConflictValue):
                lowestConflictPositions.append(j)
                
        queenPosition[i] = random.choice(lowestConflictPositions)

def diagnolConflicts(board, column, row):
    conflicts = 0
    for i in range(1,column + 1):
        if (board[column - i] == (row + i) or
            board[column - i] == (row - i)):
            conflicts = conflicts + 1           
    for i in range(column +1,8):
        if (board[i] == row + (column - i) or
            board[i] == row - (column - i)):
            conflicts = conflicts + 1
    return conflicts


def rowConflicts(board, column, row):
    conflicts = 0
    for i in range (0,column):
        if (board[i] == row):
            conflicts = conflicts + 1
    for i in range (column + 1,8):
        if (board[i] == row):
            conflicts = conflicts + 1
    return conflicts

                
def findConflicts(board, column, row):
    totalConflicts = 0
  
    rowValues = rowConflicts(board, column, row)
    diagnolValues = diagnolConflicts(board, column, row)
       
    totalConflicts = rowValues + diagnolValues
    
    return totalConflicts

def isGoalState(board):
    for i in range (0,8):
        if (findConflicts(board, i, board[i]) != 0):
            return False

    return True


def main():
    steps = 0
    while(not isGoalState(queenPosition)):
          intialize(queenPosition)
          steps += 1
    print (queenPosition)
    print (steps)




main()
