import random

class EightQueens:
    def __init__(self):
        self.queenPositions = [-99,-99,-99,-99,-99,-99,-99,-99]

    def rowConflicts(self, column, row):
        #initial number of conflicts set to 0
        conflicts = 0
        
        #search the columns before the target column
        #if a queen is in same row increment conflicts
        for col in range(0,column):
            if(self.queenPositions[col] == row):
                conflicts += 1
                
        # search the columns after the target column
        #if a queen is in the same row, increment conflicts
        for col in range(column +1,8):
            if(self.queenPositions[col] == row):
                conflicts += 1
                
        return conflicts

    def diagnolConflicts(self, column, row):
        #set initial number of conflicts to 0
        conflicts = 0

        #search columns before the target column
        #if the queen is diagnol to the target row, increment conflicts
        for col in range(1, column + 1):
            if(self.queenPositions[column - col] == (row + col) or
               self.queenPositions[column - col] == (row - col)):
                conflicts += 1

        #search columns before the target column
        #if the queen is diagnol to the target row, increment conflicts
        for col in range(column + 1,8):
            if(self.queenPositions[col] == row + (column - col) or
               self.queenPositions[col] == row - (column - col)):
                conflicts += 1

        return conflicts

    def conflictCount(self, column, row):
        # total conflicts would be the sum of the row conflicts and diagnol conflicts

        totalConflicts = 0

        totalConflicts += self.rowConflicts(column, row)
        totalConflicts += self.diagnolConflicts(column, row)

        return totalConflicts

    def inFinalState(self):
        #search through all columns
        #if the current row position in that column has conflicts
        #return false
        #else if no column has conflicts return true
        for col in range(0,8):
            if(self.conflictCount(col,self.queenPositions[col]) != 0):
                return False

        return True

    def selectLowestConflict(self, column):
        #initial lowest Conflict value will be set high
        #keep track of all positions with the current lowestConflict
        lowestConflictValue = 100
        lowestConflictPositions = []

        #for all the rows calculate the conflict
        #if conflict is lower than current conflict
        #empty list and add position to list
        #if conflict is same as current value
        #add position to list
        #if conflict is greater than current value
        #ignore
        for row in range(0,8):
            currentConflictValue = self.conflictCount(column,row)

            if(currentConflictValue < lowestConflictValue):
                lowestConflictValue = currentConflictValue
                del lowestConflictPositions[:]
                lowestConflictPositions.append(row)
                
            elif(currentConflictValue == lowestConflictValue):
                lowestConflictPositions.append(row)

        #select random position from array

        randomValue = random.choice(lowestConflictPositions)

        return randomValue

    def initialization(self):
        #for all the column randomly select a position with the minimum conflicts

        for col in range (0,8):
            self.queenPositions[col] = self.selectLowestConflict(col)
        
    def search(self):
        #randomly select a column
        #determine the smallest conflict position in that column
        col = random.randint(0,7)
        initialRow = self.queenPositions[col]
        newRow = self.selectLowestConflict(col)

        #if the state didn't change
        #then run the search again
        #else change state and finish
        if(newRow == initialRow):
            self.search()
        else:
            self.queenPositions[col] = newRow
            print(self.queenPositions)
            print("Selected Column {}, moved from {} to {}".format(col,initialRow,newRow))
        
    def returnQueens(self):
        return self.queenPositions


def main():
    board = EightQueens()
    random.seed(2)
    
    #start step counter and initilize board
    steps = 0
    board.initialization()
    print("After Initialization  {}".format(board.returnQueens()))
    
    while(not board.inFinalState()):
        board.search()
        steps += 1
        

    print("Final State   {}".format(board.returnQueens()))
    print("Number of Steps {}".format(steps))


main()
    
