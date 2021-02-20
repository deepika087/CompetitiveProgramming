__author__ = 'deepika'
import sys

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = []
        result = []
        global_max = -sys.maxint
        self.goodNodesUtil(root, result, path, global_max)
        return len(result)

    def goodNodesUtil(self, root, result, path, global_max):
        if root is None:
            return

        path += [root.val]
        if root.val >= global_max:
            result.append(root.val)
        global_max = max(root.val, global_max)
        self.goodNodesUtil(root.left, result, path, global_max )
        self.goodNodesUtil(root.right, result, path, global_max)

        if len(path) > 0:
            path.pop()

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.right=TreeNode(6)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

root1=TreeNode(1)

root2=TreeNode(3)
root2.left=TreeNode(1)
root2.right=TreeNode(4)
root2.left.left=TreeNode(3)
root2.right.left=TreeNode(1)
root2.right.right=TreeNode(5)


root3=TreeNode(3)
root3.left=TreeNode(3)
root3.left.left=TreeNode(4)
root3.left.right=TreeNode(2)
s=Solution()
print s.goodNodes(root)
print s.goodNodes(root1)
print s.goodNodes(root2)
print s.goodNodes(root3)