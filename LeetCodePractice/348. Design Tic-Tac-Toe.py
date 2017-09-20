__author__ = 'deepika'
"""
32 / 32 test cases passed.
Status: Accepted
Runtime: 75 ms
"""
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.playerscore = 1 if player == 1 else -1
        self.rows[row] = self.rows[row] + self.playerscore
        self.cols[col] = self.cols[col] + self.playerscore

        if row == col:
            self.diagonal = self.diagonal + self.playerscore

        if col == len(self.cols) - row - 1:
            self.antidiagonal = self.antidiagonal + self.playerscore

        size = len(self.rows)
        if (abs(self.rows[row]) == size or abs(self.cols[col]) == size or abs(self.diagonal) == size or abs(self.antidiagonal) == size):
            return player

        return 0









# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)