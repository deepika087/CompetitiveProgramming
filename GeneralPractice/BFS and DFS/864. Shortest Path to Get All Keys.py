__author__ = 'deepika'

# the state should not only be (x,y) but (x, y, keys)

class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])

        keysPresentInGrid = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    sr = i
                    sc = j
                elif grid[i][j] in 'abcdef':
                    keysPresentInGrid.append(grid[i][j])
        visited = []
        keysObtained = []
        return self.startBFS(grid, sr, sc, m, n, visited, keysObtained, keysPresentInGrid)


    def getValidNeighbours(self, grid, i, j, m, n, visited, keysObtained):

        result = []
        for dirs in [ [-1, 0], [1, 0], [0, -1], [0, 1]]:
            newI = i + dirs[0]
            newJ = j + dirs[1]

            if  0 <= newI < m and 0 <= newJ < n:
                if (newI, newJ) in visited:
                    continue
                if grid[newI][newJ] == '#': #Wall
                    continue
                if grid[newI][newJ] == '.' or grid[newI][newJ] in 'abcdef':
                    result.append( [ newI, newJ] )
                else: # lock
                    if chr(ord(grid[newI][newJ]) + 32) in keysObtained:
                        result.append( [ newI, newJ] )
        return result

    def startBFS(self, grid, i, j, m, n, visited, keysObtained, keysPresentInGrid):

        queue = [ [i, j] ]

        minsteps = 0
        while len(queue) > 0:
            nextLevel = []

            while len(queue) > 0:
                popped = queue.pop(0)

                if grid[popped[0]][popped[1]] in 'abcdef':
                    keysObtained.append(grid[popped[0]][popped[1]])

                if len(keysObtained) == len(keysPresentInGrid):
                    return minsteps

                neighbours = self.getValidNeighbours(grid, popped[0], popped[1], m, n, visited, keysObtained)
                if len(neighbours) > 0:
                    nextLevel.extend(neighbours)

                visited.append( (popped[0], popped[1]) )

            queue = nextLevel
            minsteps += 1
        return -1




s=Solution()
#print(s.shortestPathAllKeys(["@.a.#","###.#","b.A.B"]))
#print(s.shortestPathAllKeys(["@..aA","..B#.","....b"]))
print(s.shortestPathAllKeys(["@...a",".###A","b.BCc"]))