__author__ = 'deepika'

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxheight = max(height)
        leftMax = height[0]
        water = 0
        for i in range(1, height.index(maxheight)):
            res = (min(leftMax, maxheight) - height[i])
            water = water + res if res >= 0 else 0
            leftMax = max(leftMax, height[i])

        leftMax = height[len(height) - 1]
        for i in range(len(height) - 1, height.index(maxheight), -1):
            res = (min(leftMax, maxheight) - height[i])
            water = water + res if res >= 0 else 0
            leftMax = max(leftMax, height[i])

        return water

s=Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])



