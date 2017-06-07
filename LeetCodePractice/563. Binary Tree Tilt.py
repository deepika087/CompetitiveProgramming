__author__ = 'deepika'

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt=0
        ls=0
        rs=0
        print self.findTiltUtil(root, tilt,ls,rs)
        print "result:", ls, rs

    def findTiltUtil(self, root, tilt,ls,rs):
        if (root is None):
            return 0
        lst = self.findTiltUtil(root.left, tilt, ls, rs)
        rst = self.findTiltUtil(root.right, tilt, ls, rs)
        ls = ls + lst
        rs = rs + rst
        print "at root.data : ", root.val, ls, rs
        tilt
        if (root.left is None and root.right is None):
            return root.val
        return root.val + ls + rs

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

s=Solution()
s.findTilt(root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
#s.findTilt(root)
