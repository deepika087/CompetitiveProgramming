"""
98. Validate Binary Search Tree

74 / 74 test cases passed.
Status: Accepted
Runtime: 92 ms
"""

import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBSTUtil(self, root, max_val, min_val):
        if (root is None):
            return True
        if (root.val > max_val or root.val < min_val):
            return False
        return self.isValidBSTUtil(root.left, root.val - 1, min_val) and self.isValidBSTUtil(root.right, max_val, root.val + 1)
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTUtil(root, sys.maxint, -sys.maxint)