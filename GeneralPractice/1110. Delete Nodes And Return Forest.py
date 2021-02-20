__author__ = 'deepika'

"""
Runtime: 68 ms, faster than 52.37% of Python online submissions for Delete Nodes And Return Forest.
Memory Usage: 13.2 MB, less than 79.44% of Python online submissions for Delete Nodes And Return Forest.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = []
        self.delNodesUtil(root, to_delete, result)
        if not root.val in to_delete:
            result += [root]
        return result

    def isLeaf(self, root):
        return root.left is None and root.right is None

    def delNodesUtil(self, root, to_delete, result):
        if root is None:
            return None

        root.left = self.delNodesUtil(root.left, to_delete, result)
        root.right = self.delNodesUtil(root.right, to_delete, result)

        if root.val in to_delete:
            if root.left:
                result += [root.left]
            if root.right:
                result += [root.right]
            return None
        else:
            return root

s=Solution()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)

print(s.delNodes(root, [3,5]))