__author__ = 'deepika'


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-1
        while i >= 0:
            if nums[i] >= nums[i-1]:
                i -= 1
            else:
                break

        if i == -1:
            return sorted(nums)

        nums[len(nums) - 1], nums[i] = nums[i], nums[len(nums) - 1]
        sorted(nums[i:])

        return nums

s=Solution()
print(s.nextPermutation( nums = [1, 2, 3]))
print(s.nextPermutation( nums = [3, 2, 1]))
print(s.nextPermutation( nums = [1, 1, 5]))
print(s.nextPermutation([1]))
print(s.nextPermutation([1,2,8,4,3,7]))
