from minesweeper import Minesweeper
import unittest

class MinesweeperTest(unittest.TestCase):

    def setUp(self):
        self.fourByFourGame = "4 4\n*...\n....\n.*..\n...."

    def testNumberOfMines(self):
        self.assertEquals(2, Minesweeper.getMines(self.fourByFourGame))

unittest.main()