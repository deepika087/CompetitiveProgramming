__author__ = 'deepika'

class Solution(object):
    def findNumberOfLIS(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr)

        # Declare the list (array) for LIS and initialize LIS
        # values for all indexes
        lis = [1]*n

        # Compute optimized LIS values in bottom up manner
        for i in range (1 , n):
            for j in range(0 , i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
                    lis[i] = lis[j]+1
        print lis
        maxEle = max(lis)
        NumOfMax = list(filter(lambda x: x == maxEle, lis))
        print "NumOfMax: ", NumOfMax
        return len(NumOfMax)

s=Solution()
#print s.findNumberOfLIS([1,3,5,4,7])
print s.findNumberOfLIS([2,2,2,2,2])