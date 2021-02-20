__author__ = 'deepika'

# time limit exceeds
import sys

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, total):

        if len(nums) == 1:
            return 1
        window = nums[0]
        size = 1
        count = 0
        for i in range(1, len(nums)):
            if window * nums[i] < total:
                size = size + 1
                window = window * nums[i]

            else:
                #break window
                if size > 0:
                    print "Adding window of size: ", size
                    count = count + (size*(size+1)/2)
                window = nums[i] # give ith number a chance
                size = 1
        if size > 0:
            count = count + (size*(size+1)/2)
        return count

    def numSubarrayProductLessThanK1(self, nums, total):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        T = [ [0 for i in range(len(nums))] for j in range(len(nums))]
        nums = list(filter(lambda x: x < total, nums))

        markRowDirty = set()
        count = 0
        for k in range(1, len(nums) + 1):
            for i in range(0, len(nums)):
                j = i + k - 1
                if i in markRowDirty or j >= len(nums):
                    continue
                if i == j and nums[i] < total:
                    T[i][j] = nums[i]
                    count = count + 1
                elif i == j and nums[i] >= total:
                    T[i][j] = sys.maxint
                elif i != j:
                    if T[i][j-1] == sys.maxint:
                        markRowDirty.add(i)
                    else:
                        #print i, j
                        T[i][j] = T[i][j - 1] * nums[j]
                        if T[i][j] < total:
                            count = count + 1
                        else:
                            T[i][j] = sys.maxint
                            markRowDirty.add(i)
        #print T
        return count


s=Solution()
print s.numSubarrayProductLessThanK([1, 1, 1], 3)
print s.numSubarrayProductLessThanK([10, 5, 2, 6], 100)