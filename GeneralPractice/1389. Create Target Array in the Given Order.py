__author__ = 'deepika'

"""
Details
Runtime: 20 ms, faster than 77.41% of Python online submissions for Create Target Array in the Given Order.
Memory Usage: 13.7 MB, less than 12.81% of Python online submissions for Create Target Array in the Given Order.
"""
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        result = []
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
        return result