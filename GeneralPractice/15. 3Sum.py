from typing import List, Set


class Solution:
    def threeSum(self, nums: List[int]) -> set[str]:
        map = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i + 1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[i] + nums[right] == 0:
                    key = str(nums[i]) + '#' + str(nums[left]) + '#' + str(nums[right])
                    print(key)
                    map.add(key)
                    left += 1
                elif nums[left] + nums[i] + nums[right] < 0:
                    left += 1
                else:
                    right -=1
        return map

s=Solution()
print(s.threeSum(nums = [-1,0,1,2,-1,-4]))