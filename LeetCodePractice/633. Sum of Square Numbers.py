
"""
don't know says time exceed 100/124 still pass but similar algo in Java works absolutely fine. 
"""
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if (c == 0):
            return False
        for a in range(0, int(math.sqrt(c)) + 1 ):
            b = c - a * a
            if (self.is_sqrt(b)):
                return True
        return False

    def is_sqrt(self, b):
        return self.binary_search(0, b, b)

    def binary_search(self, s, e, n):
        if (s > e):
            return False
        mid = s + (e - s)/2
        if (mid * mid == n):
            return True
        if (mid * mid > n):
            return self.binary_search(s, mid - 1, n)
        return self.binary_search(mid + 1, e, n)

s=Solution()
print s.judgeSquareSum(7)

"""
public class Solution {
    public boolean judgeSquareSum(int c) {
        for (long a = 0; a * a <= c; a++) {
            int b = c - (int)(a * a);
            if (binary_search(0, b, b))
                return true;
        }
        return false;
    }
    public boolean binary_search(long s, long e, int n) {
        if (s > e)
            return false;
        long mid = s + (e - s) / 2;
        if (mid * mid == n)
            return true;
        if (mid * mid > n)
            return binary_search(s, mid - 1, n);
        return binary_search(mid + 1, e, n);
    }
}
"""
