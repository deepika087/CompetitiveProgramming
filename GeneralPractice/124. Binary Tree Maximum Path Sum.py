__author__ = 'deepika'

import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        global_max = -sys.maxint
        def maxPathSumHelper(root, global_max):
            if root is None:
                return 0

            leftSum = maxPathSumHelper(root.left, global_max)
            rightSum = maxPathSumHelper(root.right, global_max)

            print("Initially global max at node: " + str(root.val) + " is " + str(global_max))

            leftMax = max(leftSum, 0)
            rightMax = max(rightSum, 0)

            sum_so_far = max(root.val, root.val + leftMax + rightMax)
            global_max = max(global_max, sum_so_far)

            print("global max at node: " + str(root.val) + " is " + str(global_max))

            return sum_so_far

        maxPathSumHelper(root, global_max)
        return global_max





s=Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
print(s.maxPathSum(root1))