__author__ = 'deepika'

"""
Normal BFS won't work here. Because you want the global trees in the ordered way. If you just use the normal BfS then you would know
the local tree height only.
Think of this way that get all tree. (height, i, j) sort via height.

Now start from (0, 0) -> go to next height tree. If not possible return -1.


now from next processed tree -> go the tree just greater than the tree just processed and continue.

"""
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """

        m = len(forest)
        if m == 0:
            return -1

        n = len(forest[0])
        num_of_trees = 0
        trees = []

        for i in range(m):
            for j in range(n):
                if i!= 0 and j != 0 and forest[i][j] > 1:
                    trees.append([forest[i][j], i, j])

        sorted(trees, key=lambda x:x[0])

        sx, sy = 0, 0
        total_cost = 0
        for tree in trees:

            d = self.startBFS(sx, sy, tree[1], tree[2], m, n, forest)
            #print("Source: ", sx, sy, " Target ", tree[1], tree[2], " steps ", d)
            if d < 0:
                return -1
            total_cost += d
            sx, sy = tree[1], tree[2]
        return total_cost

        return self.startBFS(0, 0, num_of_trees, m , n, forest, visited)

    def getneighbours(self, popped, m, n, forest, visited):


        result = []
        passways = []
        for dirs in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
            newX = popped[0] + dirs[0]
            newY = popped[1] + dirs[1]

            if 0 <= newX < m and 0 <= newY < n and (newX, newY) not in visited and forest[newX][newY] > 0:
                    result.append([ forest[newX][newY], newX, newY] )
        if len(result) > 0:
            sorted(result, key=lambda x: x[0])
            return list(map(lambda x: (x[1], x[2]), result))
        else:
            return passways

    def startBFS(self, i, j, tx, ty, m, n, forest):

        queue = [(i, j)]

        steps = 0
        visited = set()

        while queue:

            nextLevel = []
            while queue:
                popped = queue.pop()

                if popped[0] == tx and popped[1] == ty:
                    return  steps

                visited.add((popped[0], popped[1]))

                neighbours = self.getneighbours(popped, m, n, forest, visited)
                if len(neighbours) > 0:
                    nextLevel += neighbours
                    #print("nextLevel: ", nextLevel)

            queue = nextLevel
            steps += 1

        return -1

s=Solution()
print(s.cutOffTree(forest = [[1,2,3],[0,0,0],[7,6,5]]))
print(s.cutOffTree(forest = [[1,2,3],[0,0,4],[7,6,5]]))
print(s.cutOffTree(forest = [[2,3,4],[0,0,5],[8,7,6]]))

