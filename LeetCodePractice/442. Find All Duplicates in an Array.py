__author__ = 'deepika'

"""
28 / 28 test cases passed.
Status: Accepted
Runtime: 356 ms

Beats 30% submission. Also x in arr is a heavy operation
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            index = nums[i] - 1 if nums[i] > 0 else -nums[i] - 1
            #print "IndeX: ", index
            if nums[index] < 0:
            #    print "At index: ", index
                number = nums[i] if nums[i] > 0 else -nums[i]
                if number not in result:
                    result.append(number)
            else:
                nums[index] = -nums[index]
        return result

s=Solution()
print s.findDuplicates([4,3,2,7,8,2,3,1])
