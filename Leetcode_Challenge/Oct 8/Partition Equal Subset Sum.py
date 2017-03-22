
"""
Not exactly the solution,
This will be solved using DFS
"""
class Solution(object):
    def canPartition(self, nums):
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1

        sumR = nums[right]
        sumL = nums[left]

        elementCovered = 2
        while(left < right):
            if (sumR == sumL and elementCovered == len(nums)):
                return True
            elif (sumR > sumL):
                left = left + 1
                sumL = sumL + nums[left]
            else:
                right = right - 1
                sumR = sumR + nums[right]
            elementCovered =  elementCovered + 1
        return False


if __name__ == "__main__":
    _s = Solution()
    s = [1, 2, 3, 5]
    print _s.canPartition(s)
    s = [1, 5, 11, 5]
    print _s.canPartition(s)