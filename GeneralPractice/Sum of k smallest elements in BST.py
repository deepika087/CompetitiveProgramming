__author__ = 'deepika'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def findkSmallestSum(self, root, k):
        count = 0
        totalSum = 0;
        self._findkSmallestSumUtil(root, k, count, totalSum)
        return totalSum

    def _findkSmallestSumUtil(self, root, k, count, totalSum):
        if root is None:
            return 0

        if (count > k):
            return 0

        totalSum += self._findkSmallestSumUtil(root.left, k, count, totalSum)

        if count >=k:
            return totalSum

        totalSum += root.val
        count += 1; # Is getting reset in every call.

        totalSum += self._findkSmallestSumUtil(root.right, k, count, totalSum)
        return totalSum



s=Solution()
t=TreeNode(10)
t.left=TreeNode(5)
t.right=TreeNode(15)
t.left.left=TreeNode(2)
t.left.right=TreeNode(7)
t.right.left=TreeNode(12)
t.right.right=TreeNode(20)
t.left.right.left=TreeNode(6)


print(s.findkSmallestSum(t, 3))