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
            if square == "*":
                output += "*"
            elif index < len(row) -1 and row[index+1] == "*":
                output += "1"
            elif index > 0 and row[index-1] == "*":
                output += "1"
            else:
                output += "0"
        return output