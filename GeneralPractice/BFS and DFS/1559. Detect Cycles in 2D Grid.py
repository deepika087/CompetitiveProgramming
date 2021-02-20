__author__ = 'deepika'

"""
Runtime: 3188 ms, faster than 50.70% of Python online submissions for Detect Cycles in 2D Grid.
Memory Usage: 250.6 MB, less than 31.25% of Python online submissions for Detect Cycles in 2D Grid.

Learnt the concept of keeping track of parents.
+ even if you have found visited. Make sure it had the value you were looking for.
"""
class Solution(object):
    result = False
    def containsCycle(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        m = len(grid)

        if m == 0:
            return False

        n = len(grid[0])
        if n == 0:
            return False

        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue
                res = self.startDFS(i, j, m, n, grid, i, j, visited, 1)
                if res:
                    return  True
        return False


    def startDFS(self, i, j, m, n, grid, par_i, par_j, visited, seen_so_far):

        visited.add( (i, j) )
        #grid[i][j] = '#'

        for dir in [ [1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx = i + dir[0]
            ny = j + dir[1]

            if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx == par_i and ny == par_j):
                continue

            if (nx, ny) in visited and seen_so_far >= 4 and grid[nx][ny] == grid[i][j]:
                    return True

            elif grid[nx][ny] == grid[i][j]:
                if (self.startDFS(nx, ny, m, n, grid, i, j, visited, seen_so_far + 1)):
                    return True
        return False

s=Solution()
print(s.containsCycle([["d","b","b"],["c","a","a"],["b","a","c"],["c","c","c"],["d","d","a"]]))
print(s.containsCycle(grid= [["b","a","c"],["c","a","c"],["d","d","c"],["b","c","c"]]))
print(s.containsCycle(grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
print(s.containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
print(s.containsCycle( grid = [["a","b","b"],["b","z","b"],["b","b","a"]]))