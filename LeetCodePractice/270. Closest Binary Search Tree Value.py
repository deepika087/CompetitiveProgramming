
"""
66 / 66 test cases passed.
Status: Accepted
Runtime: 53 ms

Beats: 72%
"""
import sys
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    result = sys.maxint
    result_val = 0
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
          return None

        def findMin(root, target):
          if abs(root.val - target) < self.result:
            self.result = abs(root.val - target)
            self.result_val = root.val

          if self.result == 0:
            self.result_val = root.val
            return self.result_val

          if target < root.val:
            return self.closestValue(root.left, target)
          else:
            return self.closestValue(root.right, target)
        findMin(root, target)
        return self.result_val
