__author__ = 'deepika'

"""
Runtime: 140 ms, faster than 19.87% of Python online submissions for Deepest Leaves Sum.
Memory Usage: 20.3 MB, less than 71.43% of Python online submissions for Deepest Leaves Sum.

I think it can be done even without dictionary. just keep track of maxheight. if at certain leaf node global max height
is less than current level. Reset sum collected so far to this leave node.
"""
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    maxHeight = -1
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leavesData = {}
        height = 0
        self.deepestLeavesSumUtil(root, height, leavesData)
        return sum(leavesData[self.maxHeight])

    def deepestLeavesSumUtil(self, root, height, leavesData):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            if height not in leavesData:
                leavesData[height] = []
            leavesData[height].append(root.val)
            self.maxHeight = max(self.maxHeight, height)


        self.deepestLeavesSumUtil(root.left, height + 1, leavesData)
        self.deepestLeavesSumUtil(root.right, height + 1, leavesData)



