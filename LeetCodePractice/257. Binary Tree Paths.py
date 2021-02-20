__author__ = 'deepika'

"""
209 / 209 test cases passed.
Status: Accepted
Runtime: 42 ms

65% better
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        self.results=[]
        self.binaryTreePathsUtil(root, path)
        return self.results

    def binaryTreePathsUtil(self, root, path):
        if root is None:
            return None

        if root.left:
            path.append(str(root.val))
            self.binaryTreePathsUtil(root.left, path)
            path.pop(-1)

        if root.right:
            path.append(str(root.val))
            self.binaryTreePathsUtil(root.right, path)
            path.pop(-1)

        if root.left is None and root.right is None:
            path.append(str(root.val))
            self.results.append("->".join(path))
            path.pop(-1)

    def binaryTreePathsUtil2(self, root, path=""):
        if root is None:
            return None

        if root.left:
            self.binaryTreePathsUtil2(root.left, str(root.val) + path)

        if root.right:
            self.binaryTreePathsUtil2(root.right, str(root.val) + path)

        if root.left is None and root.right is None:
            print root.val, " ", path


    def printAncestors(self, _p):
        self.printancestorsUtil(root, _p)

    def printancestorsUtil(self, root, _p):
        if root is None:
            return False

        if root.val == _p:
            return True

        if self.printancestorsUtil(root.left, _p) or self.printancestorsUtil(root.right, _p):
            print(root.val)
            return True


root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(6)
root.right.right.right.left=TreeNode(8)
root.right.right.right.right=TreeNode(9)

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(5)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(4)

s=Solution()
#print s.binaryTreePaths(root)
#print "--------------"
#print s.binaryTreePaths(root)

s.printAncestors(9)