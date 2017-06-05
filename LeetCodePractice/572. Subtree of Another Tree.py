"""

176 / 176 test cases passed.
Status: Accepted
Runtime: 422 ms
"""

__author__ = 'deepika'
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (t is None):
            return True

        if (s is None):
            return False

        if (self.isIdentical(s, t)):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isIdentical(self, s, t):
        if (s is None and t is None):
            return True
        if ((s is None) or (t is None)):
            return False

        return s.val == t.val and \
               self.isIdentical(s.left, t.left) and \
               self.isIdentical(s.right, t.right)




root1=TreeNode(3)
root1.left=TreeNode(4)
root1.right=TreeNode(5)
root1.left.left=TreeNode(1)
root1.left.right=TreeNode(2)

root2=TreeNode(4)
root2.left=TreeNode(1)
root2.right=TreeNode(2)

s=Solution()
print s.isSubtree(root1, root2)