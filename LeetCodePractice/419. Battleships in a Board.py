__author__ = 'deepika'

"""
28 / 28 test cases passed.
Status: Accepted
Runtime: 72 ms

Better than just 6% submissions, Since it takes O(m*n) space too.. The solution below doesn't take any extra space.

"""
class Solution(object):
    def countBattleships(self, grid):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        visited = [[ False for i in range(n)] for j in range(m)]
        ships = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'X' and visited[i][j] == False:
                    visited[i][j] = True
                    self.startDFS(grid, visited, i, j, m, n)
                    ships = ships + 1
        return ships

    def getNeighbours(self, grid, visited, i, j, m, n):

        result = []
        if i + 1 < m and not visited[i+1][j] and grid[i+1][j] == 'X':
            result.append((i+1, j))
        if j + 1 < n and not visited[i][j+1] and grid[i][j+1] == 'X':
            result.append((i, j+1))

        for (i, j) in result:
            visited[i][j] = 1

        return result

    def startDFS(self, grid, visited, i, j, m, n):
        stack = []
        stack.append((i, j))
        area = 0
        while stack:
            popped = stack.pop()
            area = area + 1
            neighbours = self.getNeighbours(grid, visited, popped[0], popped[1], m, n)
            if len(neighbours) == 0 and len(stack) == 0:
                return area

            stack += neighbours

s=Solution()
print s.countBattleships(['X..X', '...X', '...X'])

"""
class Solution(object):
    def countBattleships(self, board):
        if len(board) == 0: return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count
"""