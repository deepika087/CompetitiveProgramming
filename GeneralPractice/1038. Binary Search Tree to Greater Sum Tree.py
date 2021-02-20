__author__ = 'deepika'

# Definition for a binary tree node.
"""
Runtime: 20 ms, faster than 75.25% of Python online submissions for Binary Search Tree to Greater Sum Tree.
Memory Usage: 12.6 MB, less than 97.99% of Python online submissions for Binary Search Tree to Greater Sum Tree.
"""
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.counter = 0

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return 0

        self.bstToGst(root.right)
        self.bstToGst(root.left)

        self.counter += root.val
        root.val = self.counter
        return root

    def printTree(self, root):

        if root is None:
            return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)


root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(5)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(4)

s=Solution()
s.bstToGst(root)
s.printTree(root)

