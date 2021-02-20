__author__ = 'deepika'

"""
This is an inspired version of Leetcode 742. closest leaf in a BT.

The issue here say the tree looks like

                1
        2               3
    4       5         6     7
                    8           *
                                    *
                                        *
                                            *
                                                *
                                                    *


My idea was say we start from 6. So,
1.) Number of days to infect the subtree rooted at 6.
2.) Since 6 is in right sub tree. Number of days required to infect left subtree rooted at 2.

Take the max of two and return. However, What if the subtree at 7 is way bigger than the subtree rooted at 2.
So, we have to go to each cousin of a node to find how much time will that take.


Or another way is think of this as a BFS problem.
As in to begin with put 6 in the queue.
Then pop 6, put 3, 8 in queue because adjacent list can be infected.

Then pop 3, push 1, and 7
Then pop 8, push nothing because it is a leaf node.

"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def findLevel(self, root, target, level):
        if root is None:
            return 0, None

        if root.val == target:
            return level, root

        downLevel, tNode = self.findLevel(root.left, target, level + 1)

        if downLevel != 0:
            return downLevel, tNode

        downLevel, tNode = self.findLevel(root.right, target, level + 1)

        return downLevel, tNode

    def findMaxLevelStartingFromTarget(self, root):

        if root is None:
            return 0

        print("root: " ,root.val)

        lh = self.findMaxLevelStartingFromTarget(root.left)
        rh = self.findMaxLevelStartingFromTarget(root.right)

        return max(lh, rh) + 1

    def findMaxLevelInOppositeSubTree(self, root, target):

        if root is None:
            return -1, "Dunno"

        if root.val == target:
            return 0, "Dunno"

        l, direction = self.findMaxLevelInOppositeSubTree(root.left, target)
        if l == 0:
            print("The node is in let subtree. So, find the level in right substree.")
            return l, "left"

        r, direction = self.findMaxLevelInOppositeSubTree(root.right, target)
        if r == 0:
            print("The element is is in right sub tree. So find the level in left subtree")
            return r, "right"

        return -1, direction




    def binaryTreeInfection(self, root, target):

        level = 0
        level, targetNode = self.findLevel(root, target, level)
        print("Target: ", target, " is at level: ", level)

        daysToInfectLowTree = self.findMaxLevelStartingFromTarget(targetNode)
        print("daysToInfectLowTree: ", daysToInfectLowTree-1)

        wholeTreeLevel, direction = self.findMaxLevelInOppositeSubTree(root, target)
        if direction == "left":
            daysToInfectOppositeTree = self.findMaxLevelStartingFromTarget(root.right)
        else:
            daysToInfectOppositeTree = self.findMaxLevelStartingFromTarget(root.left)

        print("wholeTreeLevel: ", daysToInfectOppositeTree)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
root.right.left.left=TreeNode(8)
root.right.left.right=TreeNode(9)

s=Solution()
s.binaryTreeInfection(root, 6)