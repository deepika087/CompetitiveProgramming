"""
287. Find the Duplicate Number

53 / 53 test cases passed.
Status: Accepted
Runtime: 79 ms

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

class Solution(object):
    def findDuplicateUtil(self, nums, left, right):
        if (left > right):
            return
        mid = (left + right)/2

        if (mid == 0):
            return nums[mid]
        if ( (mid-1 >= 0 and nums[mid - 1] == nums[mid]) or (mid + 1 < len(nums) and nums[mid + 1] == nums[mid])):
            return nums[mid]

    def findDuplicatetemp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        self.findDuplicateUtil(nums, 0, len(nums) - 1)

    def findDuplicate(self, nums):
        checker = 0
        for item in nums:
            if (checker & 1<<item > 0):
                return item
            checker = checker | 1<<item
        return -1


s=Solution()
print s.findDuplicate([1,2, 3, 4, 5, 6, 7, 8, 7, 9])
print s.findDuplicate([2,2,2, 2])