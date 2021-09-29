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