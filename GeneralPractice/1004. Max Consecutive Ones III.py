__author__ = 'deepika'


"""
code is almost right but too convulted to understand.
Rather think of it as sliding window. If zero increase count.
if count > K
then adjust start

if count <= K
res = max(res, j - i + 1)
"""
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        result = -1

        start = 0
        end = 0

        numOfZeroes = 0
        specialcountofzeroes = 0
        firstOneAfterZero = -1

        while True:
            while end < len(A):

                if end-1 >= 0 and A[end] == 1 and A[end-1] == 0 and firstOneAfterZero == -1 : #and numOfZeroes == 1
                    firstOneAfterZero = end

                if A[end] == 0 and numOfZeroes >= K:
                        break
                if A[end] == 0:
                    numOfZeroes += 1
                    if firstOneAfterZero != -1 :
                        specialcountofzeroes += 1
                end = end + 1
            print("comparing with window ", start, " to ", end)
            if end == len(A) - 1:
                if A[end] == 1 or numOfZeroes <= K:
                    result = max(result, end - start + 1)
                else:
                    result = max(result, end - start)
            else:
                result = max(result, end - start)

            if end >= len(A)-1:
                return result

            if firstOneAfterZero == -1:
                start = end
                numOfZeroes = 1
                if K == 0:
                    while end < len(A) and A[end] == 0:
                        end += 1
                    start = end
                    numOfZeroes = 0
            else:
                start = firstOneAfterZero
                numOfZeroes = specialcountofzeroes
            firstOneAfterZero = -1 # reset everything
            specialcountofzeroes = 0

s=Solution()
print(s.longestOnes([1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1], K=8))
print(s.longestOnes(A = [1,0,1,0,0,0,1,1,1,1,0], K = 0))
print(s.longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2))
print(s.longestOnes(A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3))

