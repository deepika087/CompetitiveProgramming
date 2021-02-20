__author__ = 'deepika'


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root, target):
        length_so_far = 0
        isSeen = False
        curr_level = 0


        minDist = [float('inf')]
        def binaryTreePathsUtil(root, target, length_so_far, isSeen):
            if root is None:
                return

            if root.val == target:
                isSeen = True
                #binaryTreePathsUtil(root, target, length_so_far, isSeen)

            if root.left is None and root.right is None and isSeen:
                print("candidate: ", length_so_far, " at root: ", root.val)
                minDist[0] = min(minDist[0], length_so_far)
                return

            binaryTreePathsUtil(root.left, target, length_so_far + 1 if isSeen else length_so_far, isSeen)
            binaryTreePathsUtil(root.right, target, length_so_far + 1 if isSeen else length_so_far, isSeen)

        binaryTreePathsUtil(root, target, length_so_far, isSeen)

        def binaryTreePathsThroughParent(root, target):

            if root is None:
                return

            if root.val == target:
                return 0

            l = binaryTreePathsThroughParent(root.left, target)
            if l >= 0:
                print("Gonna search in right subtree. Root: ", root.val, " l : ", l)
                binaryTreePathsUtil(root.right, target, l+2, True)
                return l + 1

            r = binaryTreePathsThroughParent(root.right, target)
            if r >= 0:
                print("Gonna search in left subtree. Root: ", root.val,  " r : ", r)
                binaryTreePathsUtil(root.left, target, r+2, True)
                return r + 1

            return -1
        binaryTreePathsThroughParent(root, target)
        print("Min distance: ", minDist[0])


root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(6)
root.right.right.right.left=TreeNode(8)
root.right.right.right.right=TreeNode(9)

s=Solution()
s.binaryTreePaths(root, 6)