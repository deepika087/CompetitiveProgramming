__author__ = 'deepika'

"""
Submitted: Success
"""

class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
        if n == 1:
            return 1;
        if n == 2:
            return 1

        arr = [ 0 for i in range(n+1)]
        arr[0] = 0
        arr[1] = 1

        max_so_far = 1

        for i in range(2, n+1):
            if i % 2 == 0:
                arr[i] = arr[i/2]
            else:
                    arr[i] = arr[i-1] + arr[i/2 + 1]
            max_so_far = max(max_so_far, arr[i])
        # print(arr)
        return max_so_far
s=Solution()
print(s.getMaximumGenerated(0))
print(s.getMaximumGenerated(1))
print(s.getMaximumGenerated(2))
print(s.getMaximumGenerated(3))
print(s.getMaximumGenerated(7))
#[0,1,1,2,1,3,2,3]