__author__ = 'deepika'

"""
43 / 43 test cases passed.
Status: Accepted
Runtime: 135 ms
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points, key = lambda x: x[1])

        res, end = 0, -float('inf')
        for _p in points:
            if _p[0] > end:
                res = res + 1
                end = _p[1]
        return res

s=Solution()
print s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
print s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
