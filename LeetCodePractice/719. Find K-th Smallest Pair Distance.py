__author__ = 'deepika'

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)

        #http://www.geeksforgeeks.org/k-th-smallest-absolute-difference-two-elements-array/