
class Solution(object):
    """
        Naive solution. Time exceeed ultimately
    """
    def maxRotateFunction1(self, A):
        finalResult = []
        for _ in range( len(A)):
            #print " Running k = ", _
            result = 0
            for i in range( len(A) ):
                iPrime = (i + _) % len(A)
                #print " Multiplying ", iPrime, " * ", A[i]
                result = result + iPrime * A[i]
            finalResult.append(result)
        return max(finalResult)

    """
        F0 = 0 + 1a1 + 2a2 + 3a3

        F1 = F0 + a0 + a1 + a2 - 3a3 = F0 + a0 + a1 + a2 + a3 - 4a3

        F2 = F1 + a3 + a0 + a1 - 3a2 = F1 + a0 + a1 + a2 + a3 - 4a2

        F3 = F2 + a2 + a3 + a0 - 3a1 = F2 + a0 + a1 + a2 + a3 - 4a1

        This solution runs in 72 ms for 17 test cases
    """
    def maxRotateFunction1(self, A):
        finalResult = []
        F = 0
        sum = 0;
        for i in range( len(A)):
            F = F + i * A[i]
            sum = sum + A[i]
        finalResult.append(F)
        for k in range(1, len(A)):
            F = F + sum
            F = F - len(A) * A[len(A) - k ]
            finalResult.append(F)
        return max(finalResult) if len(finalResult) > 0 else 0

if __name__ == "__main__":
    nums = [4, 3, 2, 6]
    sol = Solution()
    print sol.maxRotateFunction(nums)