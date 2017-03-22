"""
80. Remove Duplicates from Sorted Array II

164 / 164 test cases passed.
Status: Accepted
Runtime: 59 ms
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        count = 0
        writer = 0
        while(i < len(nums)):
            end = i
            start = i
            #print " Start = ", start, "and  end = ", end
            while (i + 1 < len(nums) and nums[i] == nums[i+1]):
                end = end + 1
                i = i + 1

            if ( end - start >= 1):
                count = count + 2
                nums[writer] = nums[i]
                writer = writer + 1
                nums[writer] = nums[writer - 1]
                writer = writer + 1
                i = end + 1
            else:
                nums[writer] = nums[i]
                writer = writer + 1
                count = count + 1
                i = i + 1
        nums = nums[0:writer]
        return count




s=Solution()
print s.removeDuplicates([1,1,1,2,2,3])
print s.removeDuplicates([1,1,1,2])