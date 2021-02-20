__author__ = 'deepika'
"""
full time experience: Oct 18, 2017
"""

# Binary tree(Unbalanced)
# level order traversal
# 1, [2, 3] -> [ [1], [2, 3]] -> height: [0, 1]

#root : given
# Compute height of a tree
"""
def height(root):
    lh = height(root.left)
    rh = height(root.right)


for h = 0 to height
    GoToLevel(h)


class TreeNode(object):
    def __init__(self, x):
         self.val = x # int
         #self.left = None
         #self.right = None
         self.children = []

import copy
import sys
class Tree(object):

    def naryLevelTraversal(self, root):
        if root is None:
            return None

         max_width = 1 #Because at least root is present
         stack1 = list()
         stack2 = list()

         stack1.append(root)
         while True:
             while stack1: # Hold all nodes of even number levels ex: 0, 2 #stack1 hold [4, 5]
                 popped = stack1.pop(0) # 1 is popped
                 if popped.children:
                     for child in popped.children:
                         stack2.append(popped.child)

             if len(stack2) == 0:
                 break
             max_width = max(max_width, len(stack2))
             while stack2: # Holds all nodes of odd number levels ex: 1, 3
                 popped = stack2.pop(0)   # pops2, pops 3
                 if popped.children:
                     for child in popped.children:
                         stack1.append(popped.child)

             if len(stack1) == 0:
                 break
             max_width = max(max_width, len(stack1))
        return max_width



    def levelTraversal(self, root): #root -> 1
        if root is None:
            return

        result = [] # List<list<Integer>>
        self.levelTraversalUtil(root, result)

    def levelTraversalUtil(self, root, result):
        stack1 = list()        #all nodes of current level
        stack1.append(root)   #stack1 = [1]

        stack2 = list()        #all nodes of next level that are children of nodes in current level
                               #        stack2 = []
        result.append([root.val])   # result = [[1]]  O(1)
        while True:
             while stack1: # Hold all nodes of even number levels ex: 0, 2 #stack1 hold [4, 5]
                 popped = stack1.pop(0) # 1 is popped
                 if popped.left:
                     stack2.append(popped.left)   #stack2 = [2]    #Stack2 = []
                 if popped.right:
                     stack2.append(popped.right) #stack2 = [2, 3]

             if len(stack2) == 0:
                 break
             result.append([x.val for x in stack2])       # result = [ [1], [2, 3]]
             while stack2: # Holds all nodes of odd number levels ex: 1, 3
                 popped = stack2.pop(0)   # pops2, pops 3
                 if popped.left:
                     stack1.append(popped.left)    # stack1 = [4]
                 if popped.right:
                     stack1.append(popped.right)   # stack1 = [4, 5]

             if len(stack1) == 0:
                 break
             result.append([x.val for x in stack1])  # result = [[1], [2, 3], [4, 5]]
        return result


Time complexity :    O(n) #n = number of nodes in the tree
Space Complexity : O(n/2) + O(n/2) = O(n) # Two stacks


    1
   / \
  2  3
    /  \
   4   5

"""