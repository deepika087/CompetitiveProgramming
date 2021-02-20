__author__ = 'deepika'
class Solution(object):

    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        res = ""
        while N != 0:
            dividend = N / -2
            if N % 2 == 0 : #even
                res += "0"
            else:
                res += "1"
            N = dividend

        return res[::-1]

s=Solution()
print(s.baseNeg2(2))
print(s.baseNeg2(3))
print(s.baseNeg2(4))
print(s.baseNeg2(6))
print(s.baseNeg2(8))
print(s.baseNeg2(15))
