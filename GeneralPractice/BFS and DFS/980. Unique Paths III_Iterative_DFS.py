from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        empty_square = 0 # every non-obstacle square exactly once.
        if m == 0 or n == 0:
            return 0
        start, end = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 0:
                    empty_square += 1
        return self.dfs(start[0], start[1], empty_square, grid)
    def dfs(self, i, j, empty_square, grid):
        temp_visited = set()
        temp_visited.add((i, j))
        stack = [(i, j, 1, temp_visited)]
        paths = 0
        while stack:
            x,y,count,visited = stack.pop()
            #print("Exploring Neighbour: (" + str(x) + ", " + str(y) + ")", "visited = " + str(visited))
            if grid[x][y] == 2:
                if count == empty_square:
                    paths += 1
                continue
            for dir in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != -1:  # Either empty or destination
                    new_visited = visited.copy()
                    new_visited.add((nx, ny))
                    stack.append((nx, ny, count+1, new_visited))
        return paths


s = Solution()
print("Test Case 1")
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]))
print("Test Case 2")
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print("Test Case 3")
print(s.uniquePathsIII([[0, 1], [2, 0]]))
print("Test Case 4")
print(s.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
