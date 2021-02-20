__author__ = 'deepika'

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) in [0, 1]:
            return False

        sumTotal = sum(A)
        numbers = len(A)

        sumleft = A[0]
        numleft = 1
        for i in range(1, len(A)):
            sumRight = sumTotal - sumleft
            numRight = numbers - numleft

            if sumleft * numRight == sumRight * numleft:
                return True
            sumleft += A[i]
            numleft += 1
        return False

s=Solution()
print s.splitArraySameAverage([1,2,3,4,5,6,7,8])