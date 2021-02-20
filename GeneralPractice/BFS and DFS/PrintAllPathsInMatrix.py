__author__ = 'deepika'


class Solution:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.grid = [ [ 0 for _ in range(n)] for _ in range(m)]

    def start(self):

        stack=[(0, 0)]

        ways = 0

        while stack:

            popped = stack.pop()

            if popped == (self.m - 1, self.n - 1):
                ways += 1

            neigbhours = self.getNeighbours(popped)

            if len(neigbhours) > 0:
                stack += neigbhours

        return ways

    def getNeighbours(self, popped):

        right = (popped[0], popped[1] + 1) if popped[1] + 1 < self.n else None
        down = (popped[0] + 1, popped[1]) if popped[0] + 1 < self.m else None

        result = []
        if right is not None:
            result.append(right)
        if down is not None:
            result.append(down)

        return result

s=Solution(3, 3)
print(s.start())



