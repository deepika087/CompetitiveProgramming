
"""
Accepted
77 ms
Beats 47.88%
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirstOccurence(nums, target, 0, len(nums) - 1),
                self.findLastOccurence(nums, target, 0, len(nums) - 1)]

    def findFirstOccurence(self, nums, target, left, right):

        while left <= right:
            mid = int((right + left)/2)
            if nums[mid] == target:
                if mid == 0:
                    return mid
                if mid-1 >= 0 and nums[mid-1] != target:
                    return mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def findLastOccurence(self, nums, target, left, right):
        while left <= right:
            mid = int((right + left)/2)
            print(left, right, mid)
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid
                if mid + 1 < len(nums) and nums[mid + 1] != target:
                    return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

s=Solution()
print(s.searchRange([2, 2], 2))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(s.searchRange(nums = [5,7,7,8,8,10], target = 10))
print(s.searchRange([], 0))


