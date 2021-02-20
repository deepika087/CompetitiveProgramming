__author__ = 'deepika'

"""
Used BFS and DFS:
61 / 61 test cases passed.
Status: Accepted
Runtime: 92 ms

Better than 72.18%
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is not None:
            queue1 = list()
            queue2 = list()
            queue1.append(root)

            while True:
                while queue1:
                    popped = queue1.pop(0)
                    if len(queue1) == 0:
                        popped.next = None
                    else:
                        popped.next = queue1[0]

                    if popped.left:
                        queue2.append(popped.left)
                    if popped.right:
                        queue2.append(popped.right)

                while queue2:
                    popped = queue2.pop(0)
                    if len(queue2) == 0:
                        popped.next = None
                    else:
                        popped.next = queue2[0]

                    if popped.left:
                        queue1.append(popped.left)
                    if popped.right:
                        queue1.append(popped.right)

                if (len(queue1) == 0 and len(queue2) == 0):
                    break
