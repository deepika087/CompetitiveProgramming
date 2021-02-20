__author__ = 'deepika'

"""
Runtime: 20 ms, faster than 81.65% of Python online submissions for Cousins in Binary Tree.
Memory Usage: 12.7 MB, less than 70.18% of Python online submissions for Cousins in Binary Tree.
"""
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.parentX = -1
        self.parentY = -1
        self.levelX = -1
        self.levelY = -1

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """

        level = 0
        parent = -1
        return self.isCousinsUtil(root, x, y, level, parent)

    def isCousinsUtil(self, root, x, y, level, parent):

        if root is None:
            return

        #print(self.parentX, self.parentY, self.levelX, self.levelY)

        self.isCousinsUtil(root.left, x, y, level + 1, root.val)
        self.isCousinsUtil(root.right, x, y, level + 1, root.val)

        if self.parentX >= 0 and self.parentX != self.parentY and self.levelX == self.levelY:
            return True

        if root.val == x:
            self.parentX = parent
            self.levelX = level

        if root.val == y:
            self.parentY = parent
            self.levelY = level
        return False

s4=Solution()
r4=TreeNode(1)
r4.left=TreeNode(2)
r4.right=TreeNode(3)
r4.left.left=TreeNode(4)
assert s4.isCousins(r4, 4, 3) == False

s1=Solution()
r1=TreeNode(1)
r1.left=TreeNode(2)
r1.right=TreeNode(3)
r1.left.right=TreeNode(4)
r1.right.right=TreeNode(5)
assert s1.isCousins(r1, 5, 4) == True


s2=Solution()
r2=TreeNode(1)
r2.left=TreeNode(2)
r2.right=TreeNode(3)
r2.left.left=TreeNode(4)

assert s2.isCousins(r2, 2, 3) == False

"""
s3=Solution()
r3=TreeNode(4)
r3.left=TreeNode(3)
r3.left.left=TreeNode(1)
r3.left.right=TreeNode(2)
assert s3.maxSumBST(r3) == 2
"""