__author__ = 'deepika'

"""
Accepted: All test cases pass but not sure of the efficiency.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_shift_two = n << 1
        if n_shift_two > n:
            n_shift_two = n >> 1
        #print n_shift_two
        n_res = n ^ n_shift_two
        #print " And prod: ", n_res
        while n_res:
            if (n_res & 1):
                n_res = n_res >> 1
            else:
                return False
        return True

s=Solution()
print s.hasAlternatingBits(4)
print s.hasAlternatingBits(1)
print s.hasAlternatingBits(2)
print s.hasAlternatingBits(5)
print s.hasAlternatingBits(7)
print s.hasAlternatingBits(11)