__author__ = 'deepika'

"""

17 / 17 test cases passed.
Status: Accepted
Runtime: 79 ms

Better than 35%
"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.rows = len(vec2d)
        self.currentRow = 0
        self.currentCol = -1

    def next(self):
        """
        :rtype: int
        """
        #print "IndeX: (", self.currentRow, ",", self.currentCol
        return self.vec2d[self.currentRow][self.currentCol]

        #return saveR

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.vec2d) == 0 :
            return False

        if self.currentCol + 1 < len(self.vec2d[self.currentRow]):
            self.currentCol = self.currentCol + 1
            return True
        else:
            if self.currentRow + 1 < len(self.vec2d):
                self.currentRow = self.currentRow + 1
                self.currentCol = 0
                if len(self.vec2d[self.currentRow]) == 0:
                    return self.hasNext()
                return True
        return False

# Your Vector2D object will be instantiated and called as such:
vec2d = [
          [1,2],
          [3],
          [4,5,6]
        ]

vec2d_Sample2 = [[1],[]]
vec2d_Sample3 = [[1],[], [2, 3]]
i, v = Vector2D(vec2d_Sample3), []
while i.hasNext():
    v.append(i.next())
print v
