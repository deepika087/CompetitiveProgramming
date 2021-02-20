__author__ = 'deepika'

"""
74 / 74 test cases passed.
Status: Accepted
Runtime: 102 ms
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    result = None
    maxDepth = -1
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        self.finBottomUtil(root, depth)
        return self.result

    def finBottomUtil(self, root, depth):

        if root is None:
            return None

        if depth > self.maxDepth:
            self.maxDepth = depth
            #print "Updating result to :", root.val, " depth: ", self.maxDepth
            self.result = root.val

        self.finBottomUtil(root.left, depth + 1)
        self.finBottomUtil(root.right, depth + 1)


root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(5)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(4)
s=Solution()
print s.findBottomLeftValue(root2)