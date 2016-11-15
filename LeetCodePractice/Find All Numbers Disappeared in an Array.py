"""
4 / 4 test cases passed.
Status: Accepted
Runtime: 32 ms
"""

"""
For FindDuplicates
27 / 27 test cases passed.
Status: Accepted
Runtime: 885 ms
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (len(nums) == 0):
            return []
        max_num=len(nums)
        checker = 0
        result = []
        for i in range(len(nums)):
            checker = checker | 1<<nums[i]

        for i in range(1, max_num+1):
            if (checker & 1<<i > 0):
                continue
            else:
                result.append(i)
        return result

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if (len(nums) == 0):
            return []
        checker = 0
        for i in range(len(nums)):
            if ((checker & (1<<nums[i])) > 0):
                result.append(nums[i])
            checker = checker | 1<<nums[i]
        return result


s = Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])
print s.findDisappearedNumbers([1,1,2,2])
print s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
