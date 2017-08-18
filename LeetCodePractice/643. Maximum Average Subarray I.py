"""
Accepted solution: Sliding window kind of slution.

"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        sum_so_far = 0
        for i in range(k):
            sum_so_far = sum_so_far + nums[i]
        curr_sum = sum_so_far
        for i in range(k, n):
            #print('i: ', i)
            #print "popped :",
            curr_sum = curr_sum + (nums[i] - nums[i-k])
            sum_so_far = max(sum_so_far, curr_sum)
        return sum_so_far*1.0/k

s=Solution()
print s.findMaxAverage([1,12,-5,-6,50,3], 4)
