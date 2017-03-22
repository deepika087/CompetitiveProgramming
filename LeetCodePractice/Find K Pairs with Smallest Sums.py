class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        left = 0
        right = 0
        result = list()
        while(k > 0):
            if(nums1[left] <= nums2[right]):
                result.append([nums1[left], nums2[right]])
                right = right + 1
                k = k - 1
            elif ()


s=Solution()
print s.kSmallestPairs([1,7,11], [2,4,6], 3)
print s.kSmallestPairs([1,1,2], [1,2,3], 2)
print s.kSmallestPairs([1,2], [3], 3)