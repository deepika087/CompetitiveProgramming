__author__ = 'deepika'

import math

class Solution:
    def numSquares(self, n):

        nums = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]

        q, res = {n}, 0
        while True:
            qq = set()
            for e in q:
                for n in nums:
                    if e - n == 0:
                        return res + 1
                    if e - n > 0:
                        qq.add(e - n)
            q = qq
            res += 1
        return res

s=Solution()
print(s.numSquares(12))
print(s.numSquares(13))