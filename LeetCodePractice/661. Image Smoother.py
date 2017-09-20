__author__ = 'deepika'

"""
Accepted
"""
import math

class Solution(object):
    def getAverage(self, M, i, j):

        ValidNeighbours = 0
        total_sum = 0
        for _i in range(-1, 2):
            for _j in range(-1, 2):
                i_prime = i + _i
                j_prime = j + _j
                if (i_prime >= 0 and j_prime >=0 and i_prime< len(M) and j_prime < len(M[0])):
                    #print "i_prime: ", i_prime, " j_prime: ", j_prime
                    ValidNeighbours = ValidNeighbours + 1
                    total_sum = total_sum + M[i_prime][j_prime]
        return int(math.floor(total_sum/ValidNeighbours))

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        M_new = [ [0 for i in range(n)] for j in range(m)]
        for i in range(len(M)):
            for j in range(len(M[0])):
                M_new[i][j] = self.getAverage(M, i, j)
        return M_new

s=Solution()
M=[[1,1,1], [1,0,1], [1,1,1]]
#print s.imageSmoother(M)

print s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
