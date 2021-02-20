__author__ = 'deepika'

"""
Details
Runtime: 280 ms, faster than 5.16% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.
Memory Usage: 20.9 MB, less than 48.71% of Python online submissions for Sum of Nodes with Even-Valued Grandparent.
"""

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        parentVal = None
        grandParentVal = None

        self.sumEvenGrandparentUtil(root, parentVal, grandParentVal, count)
        return count[0]

    def sumEvenGrandparentUtil(self, root, parentVal, grandParentVal, count):

        if root is None:
            return

        print("Root parent GP ", root.val, parentVal, grandParentVal)
        self.sumEvenGrandparentUtil(root.left, root.val, parentVal, count)
        self.sumEvenGrandparentUtil(root.right, root.val, parentVal, count)

        if grandParentVal != None and grandParentVal % 2 == 0:
            count[0] += root.val

s4=Solution()
r4=TreeNode(6)
r4.left=TreeNode(7)
r4.right=TreeNode(8)
r4.left.left=TreeNode(2)
r4.left.right=TreeNode(7)
r4.right.left=TreeNode(1)
r4.right.right=TreeNode(3)
r4.left.left.left=TreeNode(9)
r4.left.right.left=TreeNode(1)
r4.left.right.right=TreeNode(4)
r4.right.right.right=TreeNode(5)

print(s4.sumEvenGrandparent(r4))


