__author__ = 'deepika'
"""
"""


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def printChild(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None

        lchild = self.printChild(root.left)
        rchild = self.printChild(root.right)

        if lchild is not None or rchild is not None:
            print "Node: ", root.val, " -> ", lchild , rchild

        return None if root is None else root.val

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

s=Solution()
s.printChild(root)