"""
Not all Test cases were working
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        if (root is None):
            return 0;
        tempL= root
        tempR = root
        heightL = 0
        heightR = 0
        while(tempL.left is not None):
            heightL = heightL + 1
            tempL = tempL.left
        while (tempR.right is not None):
            heightR = heightR + 1
            tempL = tempL.right
        if ( heightL == heightR):
            return (1<<heightL) -1;
        if (heightR == 1):
            return 2;
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
