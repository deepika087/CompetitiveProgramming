__author__ = 'deepika'


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        NGE = self.findNextGreaterElement(nums2)
        print(NGE)
        result = []
        hashMap = self.findMap(nums2)
        for x in nums1:
            index = hashMap[x]
            result.append(NGE[index])
        return result

    def findMap(self, T):
        hashMap = {}

        for i in range(len(T)):
            hashMap[T[i]] = i
        return hashMap

    def findNextGreaterElement(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        result = [-1 for i in range(len(T))]
        stack = [] #stack of indices

        i = 0
        while i < len(T):
            if len(stack) == 0:
                stack.append(i)
                i = i + 1
            else:
                incoming = T[i]
                topIndex = stack.pop()

                while topIndex != -1  and incoming > T[topIndex]:
                    result[topIndex] = incoming
                    if (len(stack) > 0):
                        topIndex = stack.pop()
                    else:
                        topIndex = -1
                if incoming <= T[topIndex]:
                    stack.append(topIndex)

                stack.append(i)
                i = i + 1
        return result

s=Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))