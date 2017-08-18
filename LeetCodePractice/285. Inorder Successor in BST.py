# Definition for a binary tree node.
"""
29 / 29 test cases passed.
Status: Accepted
Runtime: 139 ms
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _get_left_of(self, startPoint):
        while startPoint.left is not None:
            startPoint = startPoint.left
        return startPoint

    def _return_parent(self, root, child, rightPortion):
        succ=None
        while(root):
            if (child.val < root.val):
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if (p.right):
            return self._get_left_of(p.right)
        else:
            rightPortion = False
            if (p.val > root.val):
                rightPortion = True
            return self._return_parent(root, p, rightPortion)

root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)

root2=TreeNode(1)
root2.right=TreeNode(3)

root3 = TreeNode(3)
root3.left=TreeNode(1)
root3.right=TreeNode(4)
root3.left.right=TreeNode(2)

s=Solution()
#result = s.inorderSuccessor(root, root.left)
result = s.inorderSuccessor(root3, root3.left.right)
if result is not None:
    print result.val
else:
    print "None"
