__author__ = 'deepika'


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return 0;
        if (len(nums) == 2):
            if (nums[0] > nums[1]):
                return 0
            return 1

        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            else:
                if (nums[i] > nums[i - 1] and i + 1 < len(nums) and  nums[i] > nums[i + 1]):
                    return  i
        return 0

s=Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))