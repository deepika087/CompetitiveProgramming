__author__ = 'deepika'

"""
Runtime: 20 ms, faster than 73.79% of Python online submissions for Game of Life.
Memory Usage: 13.5 MB, less than 46.57% of Python online submissions for Game of Life.

"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        m = len(board)
        if m == 0:
            return 0

        n = len(board[0])

        for i in range(m):
            for j in range(n):

                live_neighbours = 0

                for neighbour in [ [ -1, -1], [-1, 0],[-1,1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ] :
                    r = i + neighbour[0]
                    c = j + neighbour[1]

                    if 0 <= r < m and 0 <= c < n:

                        if board[r][c] == 1 or board[r][c] == 2:
                            live_neighbours += 1

                # Following code should execute after the neighbour code
                if board[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[i][j] = 2

                if board[i][j] == 0 and live_neighbours == 3:
                    # 2 signifies the cell is now live but was originally dead.
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1
        return board


s=Solution()
print(s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))