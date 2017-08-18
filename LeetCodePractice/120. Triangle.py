__author__ = 'deepika'
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        sumT = 0
        for _ in triangle:
            sumT = sumT + min(_)
        return sumT
