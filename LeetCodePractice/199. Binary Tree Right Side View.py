__author__ = 'deepika'
"""
210 / 210 test cases passed.
Status: Accepted
Runtime: 35 ms

Better than 92.82% submissions
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         return str(self.val)

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root is None):
            return []
        result = []
        return self.rightSideViewUtil(root, result)

    def rightSideViewUtil(self, root, result):
        queue1 = [root]
        queue2 = []
        while queue1 or queue2:
            #print "queue1: ", queue1
            if len(queue1):
                result.append(queue1[-1].val)

                while len(queue1):
                    popped = queue1.pop(0)
                    if popped.left:
                        #print "Adding in queue2: ", popped.left.val
                        queue2.append(popped.left)
                    if popped.right:
                        #print "Adding in queue2: ", popped.right.val
                        queue2.append(popped.right)

            #print "queue2: ", queue2
            if len(queue2):
                result.append(queue2[-1].val)

                while len(queue2):
                    popped = queue2.pop(0)
                    if popped.left:
                        queue1.append(popped.left)
                    if popped.right:
                        queue1.append(popped.right)
        return result

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)

s=Solution()
#print s.rightSideView(root)

root=TreeNode(1)
root.left=TreeNode(2)
#root.right=TreeNode(3)
root.left.right=TreeNode(4)
#print s.rightSideView(root)

root=TreeNode(1)
root.left = None
root.right = None
#print s.rightSideView(root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
print s.rightSideView(root)

