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
                    if rowIndex < len(row) -1 and row[rowIndex+1] == "*":
                        surroundingMines += 1
                    if rowIndex > 0 and row[rowIndex-1] == "*":
                        surroundingMines += 1
                    if colIndex < len(grid) -1:
                        if grid[colIndex + 1][rowIndex] == "*":
                            surroundingMines += 1
                        if rowIndex < len(row) -1 and grid[colIndex+1][rowIndex+1] == "*":
                            surroundingMines += 1
                        if rowIndex > 0 and grid[colIndex+1][rowIndex-1] == "*":
                            surroundingMines += 1
                    if colIndex > 0 and grid[colIndex][rowIndex] == "*":
                        if grid[colIndex - 1][rowIndex] == "*":
                            surroundingMines += 1
                        if rowIndex < len(row) -1 and grid[colIndex-1][rowIndex+1] == "*":
                            surroundingMines += 1
                        if rowIndex > 0 and grid[colIndex-1][rowIndex-1] == "*":
                            surroundingMines += 1
                    output += str(surroundingMines)
        return output
        