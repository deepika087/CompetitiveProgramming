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
        if (len(nums1) * len(nums2) < k):
            k = len(nums1) * len(nums2)


        """
        Appraoch 2: Basic one. Find all pairs then sort and select top k

        25 / 27 test cases passed.
        Status: Time Limit Exceeded

        """
        for i in nums1:
            for j in nums2:
                result.append((i,j))

        def make_comparator():
            def compare(x,y):
                if (x[0] + x[1] < y[0] + y[1]):
                    return -1
                elif(x[0] + x[1] > y[0] + y[1]):
                    return 1
                else:
                    return 0
            return compare

        result = sorted(result, cmp=make_comparator())
        return result[0:k]
        #k = 0

        """
            problem with the following is that it cannot handle duplicates.If the input were absolutely sorted in ascending order
            this would work but for duplicates it fails because pointers need to be bought back
        """
        while(k > 0):
            if(nums1[left] < nums2[right]):
                result.append(([nums1[left], nums2[right]]))
                k = k - 1
                if (left + 1 < len(nums1) and right + 1 < len(nums2)):
                    if (nums1[left + 1 ] + nums2[right] < nums1[left] + nums2[right + 1]):
                        left = left + 1
                    else:
                        right = right + 1
                else:
                    if (left + 1 < len(nums1)):
                        left = left + 1
                    elif (right + 1 < len(nums2)):
                        right = right + 1
                    #else:
                    #    print " Stuck"
            elif(nums1[left] > nums2[right]):
                result.append(([nums1[left], nums2[right]]))
                k = k - 1
                if (left + 1 < len(nums1) and right + 1 < len(nums2)):
                    if (nums1[left] + nums2[right + 1] < nums1[left + 1] + nums2[right]):
                        right = right + 1
                    else:
                        left = left + 1
                else:
                    if (left + 1 < len(nums1)):
                        left = left + 1
                    elif(right + 1 < len(nums2)):
                        right = right + 1
                    #else:
                    #    print " Stuck 2"
            else:
                result.append([nums1[left], nums2[right]])
                k = k - 1
                if (left + 1 < len(nums1) and right + 1 < len(nums2)):
                    if (nums1[left] + nums2[right + 1] < nums1[left + 1] + nums2[right]):
                        right = right + 1
                    else:
                        left = left + 1
                else:
                    if (left + 1 < len(nums1)):
                        left = left + 1
                    elif(right + 1 < len(nums2)):
                        right = right + 1


        return result


s=Solution()
print s.kSmallestPairs([1,7,11], [2,4,6], 3)
print s.kSmallestPairs([1,1,2], [1,2,3], 2)
print s.kSmallestPairs([1,2], [3], 3)
print s.kSmallestPairs([1,1,2], [1,2,3], 10) #[[1,1],[1,1],[2,1],[1,2],[1,2],[2,2],[1,3],[1,3],[2,3]]


