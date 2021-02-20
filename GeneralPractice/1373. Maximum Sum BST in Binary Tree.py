__author__ = 'deepika'


"""
Runtime: 484 ms, faster than 78.72% of Python online submissions for Maximum Sum BST in Binary Tree.
Memory Usage: 81.4 MB, less than 40.42% of Python online submissions for Maximum Sum BST in Binary Tree.
"""
import sys
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def __init__(self):
        self.maxSum = -sys.maxint

    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def maxSumBSTUtil(root):
            if root is None:
                return True, 0, sys.maxint, -sys.maxint

            if root.left is None and root.right is None: #this is a potential single node BST
                self.maxSum = max(self.maxSum, root.val)
                return True, root.val, root.val, root.val


            isLeftBST, leftSum, left_min, left_max = maxSumBSTUtil(root.left)
            isRightBST, rightSum, right_min, right_max = maxSumBSTUtil(root.right)

            if isLeftBST and isRightBST and left_max < root.val < right_min :
                self.maxSum = max(self.maxSum, leftSum + root.val + rightSum)
                return True, leftSum + root.val + rightSum, min(left_min, root.val), max(right_max, root.val)
            return False, 0, sys.maxint, -sys.maxint

        maxSumBSTUtil(root)
        print(self.maxSum)
        return self.maxSum if self.maxSum >= 0 else 0

s4=Solution()
r4=TreeNode(-2)
r4.left=TreeNode(-1)
r4.right=TreeNode(-3)
assert s4.maxSumBST(r4) == 0

s1=Solution()
r1=TreeNode(2)
r1.left=TreeNode(1)
r1.right=TreeNode(3)
assert s1.maxSumBST(r1) == 6

s2=Solution()
r2=TreeNode(5)
r2.left=TreeNode(4)
r2.right=TreeNode(8)
r2.left.left=TreeNode(3)
r2.right.left=TreeNode(6)
r2.right.right=TreeNode(3)
assert s2.maxSumBST(r2) == 7

s3=Solution()
r3=TreeNode(4)
r3.left=TreeNode(3)
r3.left.left=TreeNode(1)
r3.left.right=TreeNode(2)
assert s3.maxSumBST(r3) == 2

