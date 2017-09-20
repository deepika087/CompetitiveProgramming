__author__ = 'deepika'

"""
300 / 300 test cases passed.
Status: Accepted
Runtime: 39 ms

Better than : 50%
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        n_new = n if n >= 0 else -n
        res = self.myPowUtil(x, n_new)
        if n < 0:
            return 1/res
        return res

    def myPowUtil(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == 2:
            return x*x

        if n%2 == 1:
            res = self.myPow(x, (n-1)/2)
            return x * res * res
        else:
            res = self.myPow(x, (n)/2)
            return res * res