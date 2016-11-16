"""
268. Missing Number
Used Binary search. Rather than this I could have used xor thing becuase numbers are not necessarily sorted.
121 / 121 test cases passed.
Status: Accepted
Runtime: 65 ms
"""
class Solution(object):
    def missingNumberUtil(self, nums, left, right):
        if (left > right):
            return left
        mid =  (right + left)/2
        if ( (mid == 0 and nums[mid] == 1) or (nums[mid] - mid == 1 and nums[mid-1] == mid-1)):
            return mid
        if (nums[mid] == mid): #Go right
            return self.missingNumberUtil(nums, mid + 1, right)
        else:
            return self.missingNumberUtil(nums, left, mid - 1)

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        if (len(nums) == 1):
            if (nums[0] == 0):
                return 1
            if (nums[0] == 1):
                return 0;
        return self.missingNumberUtil(nums, 0, len(nums) - 1)

s=Solution()
print s.missingNumber([0, 1, 3])