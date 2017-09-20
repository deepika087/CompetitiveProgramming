__author__ = 'deepika'

"""
61 / 61 test cases passed.
Status: Accepted
Runtime: 135 ms
"""
class Solution(object):
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths(self, m, n):
        count = [[0 for x in range(n)] for y in range(m)]
        print count
        # Count of paths to reach any
        # cell in first column is 1
        for i in range(m):
            count[i][0] = 1;

        # Count of paths to reach any
        # cell in first column is 1
        for j in range(n):
            count[0][j] = 1;
        print count
        if m == 1 or n == 1:
            return count[m-1][n-1]
        # Calculate count of paths for other
        # cells in bottom-up
        # manner using the recursive solution
        for i in range(1, m):
            for j in range(n):
                print "Assigning value to : ", i, j
                count[i][j] = count[i-1][j] + count[i][j-1]
        return count[m-1][n-1]

s=Solution()
print s.uniquePaths(2, 1)