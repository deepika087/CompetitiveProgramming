__author__ = 'deepika'

"""

149 / 149 test cases passed.
Status: Accepted
Runtime: 52 ms
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = x^y
        count = 0
        while(res > 0):
            if (res & 1):
                count = count + 1
            res = res >> 1
        return count

s=Solution()
print s.hammingDistance(1, 4)