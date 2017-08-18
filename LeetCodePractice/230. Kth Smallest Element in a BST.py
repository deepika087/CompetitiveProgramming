__author__ = 'deepika'

"""
91 / 91 test cases passed.
Status: Accepted
Runtime: 72 ms

91.1% better. I think catch here is breaking when *if self.result is not None:*
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    count = 0
    result = None
    def kthSmallestUtil(self, root, k):
        if root is None:
            return
        if self.result is not None:
            return self.result

        self.kthSmallestUtil(root.left, k)
        self.count = self.count + 1
        if (self.count == k):
            self.result = root.val
            return root.val
        self.kthSmallestUtil(root.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.kthSmallestUtil(root, k)
        return self.result




root1=TreeNode(9)
root1.left=TreeNode(7)
root1.left.left=TreeNode(6)
root1.left.right=TreeNode(8)
root1.right=TreeNode(10)

s=Solution()
print s.kthSmallest(root1, 3)

