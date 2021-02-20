__author__ = 'deepika'

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse(self,root):
        if root is None:
            return

        print(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


t=TreeNode("king")
t.left=TreeNode("a1")
t.right=TreeNode("a2")
t.left.left=TreeNode("b1")
t.left.right=TreeNode("b2")
t.right.left=TreeNode("c1")
t.right.right=TreeNode("c2")
t.left.left.left=TreeNode("d1")
t.left.left.right=TreeNode("d2")
t.left.right.right=TreeNode("d3")

s=Solution()
print(s.traverse(t))
