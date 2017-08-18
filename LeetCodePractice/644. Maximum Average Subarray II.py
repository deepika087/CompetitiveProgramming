"""
time limit exceeds
"""
import sys
class Solution(object):
    """
    Will find max subarray of size k
    """
    def findMaxsumOfK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #print "Finding max subarray of size : ", k
        n = len(nums)
        sum_so_far = 0
        for i in range(k):
            sum_so_far = sum_so_far + nums[i]
        curr_sum = sum_so_far
        for i in range(k, n):
            curr_sum = curr_sum + (nums[i] - nums[i-k])
            sum_so_far = max(sum_so_far, curr_sum)
        return sum_so_far

    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if (len(nums) == 1):
            return nums[0]*1.0
        if (len(nums) == k):
            return sum(nums)*1.0/k
        max_avg = -sys.maxint
        for i in range(k, len(nums)):
            avg_of_step = self.findMaxsumOfK(nums, i)*1.0/i
            max_avg = max(avg_of_step, max_avg)
        return max_avg

s=Solution()
print s.findMaxAverage([4,0,4,3,3], 5)
print s.findMaxAverage([1,12,-5,-6,50,3], 4)
