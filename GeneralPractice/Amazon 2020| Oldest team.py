__author__ = 'deepika'


"""
 President =
	              20
          12            18

      11   2   3      15   8
Output = 18

Explanation :
There are three managers in this tree with the following team tenures :
12 => (11+2+3+12)/4 = 7
18 => (18+15+8)/3 = 13.67
20 => (12+11+2+3+18+15+8+20)/8 = 11.125

Time complexity : O(n)

Intution: Each node will give its parent the info about sum seen so far + number of elements seen in that subtree.
Leaves will send just the value of node and count = 1.

One implementation uses additional DS called Node. there is another implementation without using extra DS.
"""

class Node:
    def __init__(self):
        self.N = 0
        self.sum_so_far = 0


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        self.maxExperience = -float('inf')
        self.nodeWithMaxExperience =  -float('inf')

    def findMostExperiencedTeam(self, tree):

        def fmetUtil(tree):

            if tree is None:
                return Node()

            if tree.left is None and tree.right is None:
                n = Node()
                n.N = 1
                n.sum_so_far = tree.val
                return n

            nodeL = fmetUtil(tree.left)
            nodeR = fmetUtil(tree.right)

            currExp = (nodeL.sum_so_far + nodeR.sum_so_far + tree.val)/(nodeL.N + nodeR.N + 1)

            if currExp > self.maxExperience:
                self.maxExperience = currExp
                self.nodeWithMaxExperience = tree.val

            n = Node()
            n.N = nodeL.N + nodeR.N + 1
            n.sum_so_far = nodeL.sum_so_far + nodeR.sum_so_far + tree.val
            return n

        fmetUtil(tree)
        return self.nodeWithMaxExperience

    def findMostExperiencedTeamWithoutDS(self, tree):

        def fmetwDS(tree):
            if tree is None:
                return [0, 0]

            if tree.left is None and tree.right is None:
                return [tree.val, 1]

            leftSum, leftCount =  fmetwDS(tree.left)
            rightsum, rightCount = fmetwDS(tree.right)

            currExp = (leftSum + rightsum + tree.val)/(leftCount + rightCount + 1)

            if currExp > self.maxExperience:
                self.maxExperience = currExp
                self.nodeWithMaxExperience = tree.val

            return [leftSum + rightsum + tree.val, leftCount + rightCount + 1]

        fmetwDS(tree)
        return self.nodeWithMaxExperience

root1=TreeNode(1)
root1.left=TreeNode(2)
root1.left.left=TreeNode(3)
root1.left.left.left=TreeNode(4)
s1=Solution()
print(s1.findMostExperiencedTeam(root1))

root2=TreeNode(1)
root2.left=TreeNode(2)
root2.right=TreeNode(5)
root2.left.left=TreeNode(3)
root2.left.right=TreeNode(4)

s2=Solution()
print(s2.findMostExperiencedTeamWithoutDS(root2))







