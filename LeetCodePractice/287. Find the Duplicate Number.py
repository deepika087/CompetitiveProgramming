__author__ = 'deepika'

"""
53 / 53 test cases passed.
Status: Accepted
Runtime: 82 ms

Beats 9% only
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for i in nums:
            if (counter & 1<<i > 0):
                return i
            counter = counter | 1<<i
