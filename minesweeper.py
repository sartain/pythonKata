class Minesweeper:
    
    #Take string input of board
    #Line breaks specify lines
    def getMines(self, board):
        rows = board.split("\n")
        mineCount = 0
        for row in rows:
            for square in row:
                if square == "*":
                    mineCount += 1
        return mineCount

    def convertRowToOutput(self, board):
        grid = board.split("\n")
        output = ""
        for colIndex, row in enumerate(grid):
            if output != "":
                output += "\n"     
            for rowIndex, square in enumerate(row):
                surroundingMines = 0
                if square == "*":
                    output += "*"
                else:
                    surroundingMines = self.getSurroundingMines(colIndex, rowIndex, grid, row)
                    output += str(surroundingMines)
        return output

    def getSurroundingMines(self, colIndex, rowIndex, grid, row):
        surroundingMines = 0
        if rowIndex < len(row) - 1:
            surroundingMines += self.getLeftRightMines(rowIndex+1, colIndex, grid)
            surroundingMines += self.getAboveAndBelowMines(rowIndex+1, colIndex, grid)
        if rowIndex > 0:
            surroundingMines += self.getLeftRightMines(rowIndex-1, colIndex, grid)
            surroundingMines += self.getAboveAndBelowMines(rowIndex-1, colIndex, grid)
        if colIndex > 0:
            surroundingMines += self.getLeftRightMines(rowIndex, colIndex - 1, grid)
        if colIndex < len(grid) -1:
            surroundingMines += self.getLeftRightMines(rowIndex, colIndex + 1, grid)
        return surroundingMines

    def getAboveAndBelowMines(self, rowIndex, colIndex, grid):
        surroundingMines = 0
        if colIndex > 0:
            surroundingMines += self.getLeftRightMines(rowIndex, colIndex-1, grid)
        if colIndex < len(grid) - 1:
            surroundingMines += self.getLeftRightMines(rowIndex, colIndex+1, grid)
        return surroundingMines

    def getLeftRightMines(self, rowIndex, colIndex, grid):
        surroundingMines = 0
        if grid[colIndex][rowIndex] == "*":
            surroundingMines += 1
        return surroundingMines
        