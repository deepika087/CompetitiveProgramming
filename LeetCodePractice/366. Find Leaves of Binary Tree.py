__author__ = 'deepika'
"""

68 / 68 test cases passed.
Status: Accepted
Runtime: 69 ms
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.findLeavesUtil(root, result)
        print result

    def findLeavesUtil(self, root, result):
        if root is None:
            return 0
        lvl = 1 + max(self.findLeavesUtil(root.left, result), self.findLeavesUtil(root.right, result))
        print root.val, " ", lvl
        if (len(result) < lvl):
            result.append([])
        result[lvl - 1].append(root.val)
        return lvl



root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

root2=TreeNode(3)
root2.left=TreeNode(2)
root2.right=TreeNode(5)
root2.left.left=TreeNode(1)
root2.left.right=TreeNode(0)

s=Solution()
print s.findLeaves(root2)