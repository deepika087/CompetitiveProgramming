__author__ = 'deepika'

"""This is a wrong approach. It can be solved by DP
"""
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N == 3:
            return 3
        if N == 4:
            return 4
        if N == 5:
            return 5

        n_half = N/2
        remaining_v = N - n_half - 2
        return n_half * (remaining_v + 1)

s=Solution()
for i in range(1, 51):
    print " For i = ", i, " ", s.maxA(i)
