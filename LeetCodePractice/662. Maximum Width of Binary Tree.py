__author__ = 'deepika'
"""
Time limit exceeds for large input
"""

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         return str(self.val)

class Solution(object):

    def getActualLen(self, q):
        #print "Queue:", q
        while q and q[0] is None:
            q.pop(0)
        while q and q[-1] is None:
            q.pop(-1)
        return len(q)

    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue1 = []
        queue2 = []
        queue1.append(root)
        result = []
        len1 = self.getActualLen(queue1)
        while(len(queue1) or len(queue2)):
            result.append(len1)
            while (len(queue1) > 0):
                popped = queue1.pop(0)
                if popped:
                    #if (popped.left):
                    queue2.append(popped.left)
                    #if (popped.right):
                    queue2.append(popped.right)
                else:
                    queue2.append(None)
                    queue2.append(None)

            len2 = self.getActualLen(queue2)
            if (len2 == 0 ):
                break

            result.append(len2)
            while(len(queue2) > 0):
                popped = queue2.pop(0)
                if popped:
                    #if (popped.left):
                    queue1.append(popped.left)
                    #if (popped.right):
                    queue1.append(popped.right)
                else:
                    queue1.append(None)
                    queue1.append(None)
            #print "queue1: ", queue1
            len1 = self.getActualLen(queue1)
            if (len1 == 0):
                break
        #print result
        return max(result)

s=Solution()
root=TreeNode(3)
root.left=TreeNode(2)
root.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right.right=TreeNode(5)
assert (s.widthOfBinaryTree(root) == 4)

root2=TreeNode(1)
root2.left=TreeNode(3)
root2.right=TreeNode(2)
root2.left.left=TreeNode(5)
root2.left.right=TreeNode(3)
root2.right.right=TreeNode(9)
assert (s.widthOfBinaryTree(root2) == 4)

root3=TreeNode(1)
root3.left=TreeNode(3)
root3.right=TreeNode(2)
root3.left.right=TreeNode(3)
root3.right.left=TreeNode(1)
root3.right.right=TreeNode(9)
assert (s.widthOfBinaryTree(root3) == 3)

root4=TreeNode(1)
root4.left=TreeNode(3)
root4.right=TreeNode(2)
root4.left.left=TreeNode(4)
assert (s.widthOfBinaryTree(root4) == 2)

root5=TreeNode(1)
root5.left=TreeNode(1)
root5.right=TreeNode(1)
root5.left.left=TreeNode(1)
root5.left.left.left=TreeNode(1)
root5.right.right=TreeNode(1)
root5.right.right.right=TreeNode(1)

assert (s.widthOfBinaryTree(root5) == 8)

