__author__ = 'deepika'

# Definition for a binary tree node.

"""
Runtime: 176 ms, faster than 9.42% of Python online submissions for Convert BST to Greater Tree.
Memory Usage: 17.1 MB, less than 61.59% of Python online submissions for Convert BST to Greater Tree.
"""
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    postOrderSum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        self.convertBSTUtil(root)
        return root

    def convertBSTUtil(self, root):
        if root is None:
            return 0


        self.convertBSTUtil(root.right)
        print("First step ", root.val )
        self.postOrderSum+= root.val
        root.val = self.postOrderSum
        print(root.val, " ", self.postOrderSum )

        self.convertBSTUtil(root.left)





root=TreeNode(2)
root.left=TreeNode(0)
root.right=TreeNode(3)
root.left.left=TreeNode(-4)
root.left.right=TreeNode(1)
s=Solution()
s.convertBST(root)