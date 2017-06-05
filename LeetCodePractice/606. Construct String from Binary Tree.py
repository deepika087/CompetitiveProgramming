__author__ = 'deepika'

"""
162 / 162 test cases passed.
Status: Accepted
Runtime: 136 ms
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result=[]
        self.tree2strUtil(t, result)
        #print "done"
        result=map(lambda x:str(x), result)
        return ''.join(result)

    def tree2strUtil(self, t, result):
        if (t is None):
            return None
        result.append(t.val)
        if (t.left is not None or t.right is not None):
            result.append("(")
            self.tree2strUtil(t.left, result)
            result.append(")")

        else:
            self.tree2strUtil(t.left, result)

        if (t.right is None):
            self.tree2strUtil(t.right, result)
        else:
            result.append("(")
            self.tree2strUtil(t.right, result)
            result.append(")")

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)

s=Solution()
s.tree2str(root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
s.tree2str(root)
