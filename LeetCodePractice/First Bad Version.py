
"""

21 / 21 test cases passed.
Status: Accepted
Runtime: 35 ms

"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if (version >= 1):
        return True
    return False

class Solution(object):
    def firstBadVersionUtil(self, start, end):
        if (start > end):
            return
        mid = (end + start)/2
        if (isBadVersion(mid)):
            if (mid == 1):
                return mid
            if (mid - 1 > 0 and not isBadVersion(mid - 1)):
                return mid
            else:
                return self.firstBadVersionUtil(start, mid - 1)
        else:
            return self.firstBadVersionUtil(mid + 1, end)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 0):
            return 0
        if (n == 1):
            return 1

        return self.firstBadVersionUtil(1, n)
s=Solution()
#print s.firstBadVersion(10)
print s.firstBadVersion(2)