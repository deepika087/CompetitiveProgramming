__author__ = 'deepika'
"""
Just 22% better.

21 / 21 test cases passed.
Status: Accepted
Runtime: 86 ms
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroPtr = 0
        while zeroPtr < len(nums) and nums[zeroPtr] != 0:
                zeroPtr = zeroPtr + 1

        nonZeroPtr = zeroPtr + 1
        while nonZeroPtr < len(nums) and nums[nonZeroPtr] == 0:
                nonZeroPtr = nonZeroPtr + 1

        while True:
            if nonZeroPtr in [len(nums), len(nums) + 1, len(nums) ]:
                break
            nums[zeroPtr] = nums[nonZeroPtr]
            zeroPtr = zeroPtr + 1

            nonZeroPtr = nonZeroPtr + 1
            while nonZeroPtr < len(nums) and nums[nonZeroPtr] == 0:
                nonZeroPtr = nonZeroPtr + 1



        #zeroPtr = zeroPtr + 1
        while zeroPtr < len(nums):
            nums[zeroPtr] = 0
            zeroPtr = zeroPtr + 1
        print nums

s=Solution()
s.moveZeroes([0, 1, 0, 3, 12])
s.moveZeroes([1, 2, 3, 0, 4, 0, 5])
s.moveZeroes([0, 0, 0, 1, 2, 3, 0, 4, 0, 5])
