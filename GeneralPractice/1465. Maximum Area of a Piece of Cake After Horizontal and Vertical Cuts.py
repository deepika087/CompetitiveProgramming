__author__ = 'deepika'

import sys

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """

        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)

        horizontal_max = self.max_difference(horizontalCuts, h)
        vertical_max = self.max_difference(verticalCuts, w)

        return horizontal_max * vertical_max


    def max_difference(self, array, dimension):
        max_diff = max(array[0], dimension - array[len(array) - 1])

        for i in range(0, len(array) - 1):
            max_diff = max(max_diff, array[i+1] - array[i])

        return max_diff

s=Solution()
print(s.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(s.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
print(s.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))