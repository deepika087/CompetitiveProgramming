__author__ = 'deepika'
#not owkring

# 687. Longest Univalue Path

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    result = 0
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.longestUnivaluePathUtil(root)
        return self.result

    def longestUnivaluePathUtil(self, root):
        if root is None:
            return None, 0

        lchild, leftLen = self.longestUnivaluePathUtil(root.left)
        rchild, rightLen = self.longestUnivaluePathUtil(root.right)

        if lchild == root.val:
            leftLen = leftLen + 1
        if rchild == root.val:
            rightLen = rightLen + 1


        self.result = max(self.result, leftLen + rightLen)
        print "At node: ", root.val, "left: ", leftLen, "right :", rightLen, " result: ", self.result
        return root.val, max(leftLen, rightLen)

s=Solution()
root=TreeNode(1)
root.left=TreeNode(4)
root.right=TreeNode(5)
root.left.left=TreeNode(4)
root.left.right=TreeNode(4)
root.right.right=TreeNode(5 )

root2=TreeNode(5)
root2.left=TreeNode(4)
root2.right=TreeNode(5)
root2.left.left=TreeNode(1)
root2.left.right=TreeNode(1)
root2.right.right=TreeNode(5)

print s.longestUnivaluePath(root)
print s.longestUnivaluePath(root2)
