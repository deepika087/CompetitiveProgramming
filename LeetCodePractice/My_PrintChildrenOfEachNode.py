__author__ = 'deepika'
"""
"""


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def printChild(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None

        lchild = self.printChild(root.left)
        rchild = self.printChild(root.right)

        if root.left is None  and root.right is None:
            return root.val
        else:
            print "Node: ", root.val, " -> ", lchild , rchild
            return root.val
            #root.val = (lchild if lchild is not None else 1) * (rchild if rchild  is not None else 1)

        #return None  else root.val

    def binaryTreePaths(self, root):
        if root is None:
          return None
        result = []
        self.printUtil(root, result)

    def printUtil(self, root, result):
        if root is None:
            return

        result.append(root.val)
        if root.left is None and root.right is None:
            print result
            #result.pop() <
            return


        self.printUtil(root.left, result)
        if root.left: # <- important check otherwise pop is done even when not required.
            result.pop()

        self.printUtil(root.right, result)
        if root.right:
            result.pop()



root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(10)
root.left.right=TreeNode(9)
root.right.right=TreeNode(5)

root2=TreeNode(3)
root2.left=TreeNode(2)
root2.right=TreeNode(6)
root2.left.left=TreeNode(1)
root2.left.right=TreeNode(5)
root2.right.right=TreeNode(7)
root2.right.left=TreeNode(8)
root2.right.left.right=TreeNode(9)



s=Solution()
print "Before: "
s.binaryTreePaths(root)
s.printChild(root)
print "after: "
s.binaryTreePaths(root2)



"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def printPaths(self, root, path_so_far, result):
        if (root is None):
            return

        self.printPaths(root.left,path_so_far +  "->" + str(root.val), result)
        self.printPaths(root.right, path_so_far + "->" + str(root.val), result)

        if (root.left is None and root.right is None):
            if (result is not None):
                result.append(path_so_far[2:] + "->" + str(root.val))

    def binaryTreePaths(self, root):
        path_so_far=""
        result=[]
        self.printPaths(root, path_so_far, result)
        if (len(result) > 0 and result[0][0:2] == "->"):
            return list(result[0][2:])
        else:
            return result
"""