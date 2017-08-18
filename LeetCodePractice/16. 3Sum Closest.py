"""
125 / 125 test cases passed.
Status: Accepted
Runtime: 112 ms
"""
import sys

class Solution(object):
    def _decide(xPlusy, target_prime, delta_lowest, target):
        if (target <= 0):
            return (xPlusy - target_prime) > delta_lowest

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # idea is x + y should close to target - nums[i]
        nums = sorted(nums)
        closest_sum = sys.maxint
        delta_lowest = sys.maxint
        for i in range(len(nums)):
            target_prime = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right and left < len(nums)):
                xPlusy = nums[left] + nums[right]
                if (xPlusy == target_prime):
                    return xPlusy + nums[i]
                if (abs(xPlusy - target_prime) < delta_lowest):
                    closest_sum = xPlusy + nums[i]
                    delta_lowest = abs(xPlusy - target_prime)

                if (xPlusy > target_prime):
                    right = right - 1
                else:
                    left = left + 1
        return closest_sum

s=Solution()
print s.threeSumClosest([-1, 2, 1, -4], 1)
print s.threeSumClosest([1,1,1,0], -100)
