import sys
import math

class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        grid = [ [0 for i in range(width)]  for j in range(height)]
        totalRes = 0
        while self.moreNuts(nuts):
            minIndex = self.getTargetNutPosition(grid, nuts, squirrel, tree)
            print "---Selected Nut: ", nuts[minIndex]
            res, newsquirrel = self.traverseToPos(grid, squirrel, tree, nuts[minIndex])
            nuts.pop(minIndex)
            totalRes += res
            squirrel = newsquirrel
        return totalRes


    def traverseToPos(self, grid, squirrel, tree, targetNut):
        steps1 = self.actualTraverse(grid, squirrel, targetNut)
        print "From start to nuts in ", steps1, "steps"
        steps2 = self.actualTraverse(grid, targetNut, tree)
        print "From nut to tree in ", steps2, "steps"
        return steps1 + steps2, tree

    def moreNuts(self, nuts):
        return len(nuts) > 0

    def getTargetNutPosition(self, grid, nuts, squirrel, tree):
        minIndex = -1
        minDist = sys.maxint
        for i in range(len(nuts)):
          dist = self.findDist(squirrel, nuts[i])
          dist += self.findDist(nuts[i], tree)
          if dist < minDist:
            dist = minDist
            minIndex = i
        return minIndex

    def findDist(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]);
        #return math.sqrt((start[0] - end[0])*(start[0] - end[0]) + (start[1] - end[1])* (start[1] - end[1]))
        
    def getneighbours(self, grid, start):
        x = start[0]
        y = start[1]
        result = []
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i == 0 and j == 0:
                    continue
                if i == 1 and j == -1 or i == 1 and j == 1 or i == -1 and j == -1 or i == -1 and j == 1:
                    continue
                newx = x + i
                newy = y + j
                if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]):
                    continue
                else:
                    result.append((newx, newy))
        return result

    def getNearestNeighbour(self, targetNut, neighbours):
        def myComparator():
            def compare(x, y):
                if (abs(x[1] - targetNut[1]) < abs(y[1] - targetNut[1])):
                    return -1
                elif (abs(x[1] - targetNut[1]) > abs(y[1] - targetNut[1])):
                    return 1
                else: #if y component in equal
                    if (abs(x[0] - targetNut[0]) < abs(y[0] - targetNut[0])):
                        return -1
                    elif (abs(x[0] - targetNut[0]) > abs(y[0] - targetNut[0])):
                        return 1
                    return 0
            return compare
        neighbours = sorted(neighbours, cmp=myComparator())
        print "Neighbours : ", neighbours
        return neighbours[0]







    def actualTraverse(self, grid, start, targetNut):
        stack = []
        stack.append(start)
        steps = 0
        while stack:
            popped = stack.pop()
            if (popped[0] == targetNut[0] and popped[1] == targetNut[1]):
                break
            neighbours = self.getneighbours(grid, popped)
            _neighbour = self.getNearestNeighbour(targetNut, neighbours)
            steps = steps + 1

            stack += [_neighbour]
        return steps
        #print "Reached in ", step, " steps"


s=Solution()
s.minDistance(5, 7, [2,2], [4,4], [[3,0], [2,5]])