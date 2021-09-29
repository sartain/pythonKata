from minesweeper import Minesweeper
import unittest

class MinesweeperTest(unittest.TestCase):

    def setUp(self):
        self.fourByFourGame = "4 4\n*...\n....\n.*..\n...."

    def testNumberOfMines(self):
        self.assertEquals(2, Minesweeper().getMines(self.fourByFourGame))

    def testSurroundingMines(self):
        self.assertEquals("01*10", Minesweeper().convertRowToOutput("..*.."))

    def testTwoMinesSurrounding(self):
        self.assertEquals("*2*", Minesweeper().convertRowToOutput("*.*"))

    def testMineBelowSurrounding(self):
        self.assertEquals("111\n1*1", Minesweeper().convertRowToOutput("...\n.*."))
unittest.main()