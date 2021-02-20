__author__ = 'deepika'

"""
Accepted
"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.floodFillUtil(image, sr, sc, newColor)
        return image

    def getNeighbours(self, image, sr, sc, newColor, startColor):
        m = len(image)
        n = len(image[0])

        print "Finding for...", sr, sc
        x_axis = [ -1, 1, 0, 0]
        y_axis = [ 0, 0, -1, 1]
        x = sr
        y = sc
        result = []
        for i in range(len(x_axis)):
            i_prime = x + x_axis[i]
            j_prime = y + y_axis[i]

            print "Proposal : ", i_prime, j_prime
            if i_prime < 0 or i_prime >= m or j_prime < 0 or j_prime >= n or image[i_prime][j_prime] == newColor:
                continue
            if image[i_prime][j_prime] == startColor:
                result.append((i_prime, j_prime))
        return result


    def floodFillUtil(self,image, sr, sc, newColor):
        startColor = image[sr][sc]
        queue = [(sr, sc)]

        while queue:
            popped = queue.pop(0)
            image[popped[0]][popped[1]] = newColor

            neighbours = self.getNeighbours(image, popped[0], popped[1], newColor, startColor)
            print "Neighbours for ", popped, " are ", neighbours
            if len(neighbours) >= 1:
                queue += neighbours

s=Solution()
print s.floodFill([[0,0,0],[0,1,1]],
1,
1,
1)

#print s.floodFill([[0,0,0],[0,0,0]],0, 0, 2)
#print s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)