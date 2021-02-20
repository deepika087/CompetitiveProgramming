__author__ = 'deepika'
import sys
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         return str(self.val)


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findSecondMinimumValueUtil(root)

    def findSecondMinimumValueUtil(self, root):
        if root is None:
            return None

        #left_minimum, right_minimum = sys.maxint, sys.maxint
        left_minimum = self.findSecondMinimumValueUtil(root.left)
        right_minimum= self.findSecondMinimumValueUtil(root.right)

        if root.left is None and root.right is None:
            return root.val

        if root.left and root.right:
            return self._second_min(root.val, left_minimum, right_minimum)

        print "left_minimum: ", left_minimum, "right_minimum: ", right_minimum

    def _second_min(self, a, b, c):
         pass


s=Solution()
root=TreeNode(2)
root.left=TreeNode(2)
root.right=TreeNode(5)
root.right.left=TreeNode(5)
root.right.right=TreeNode(7)
s.findSecondMinimumValue(root)