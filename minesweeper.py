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

    def convertRowToOutput(self, row):
        output = ""
        for index, square in enumerate(row):
            #Check behind
            #Check ahead
            surroundingMines = 0
            if square == "*":
                output += "*"
            else:
                if index < len(row) -1 and row[index+1] == "*":
                    surroundingMines += 1
                if index > 0 and row[index-1] == "*":
                    surroundingMines += 1
                output += str(surroundingMines)
        return output