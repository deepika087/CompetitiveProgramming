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

    def findIndex(self, str, si, ei):
        if (si > ei):
            return -1;

        s = []

        for i in range(si, ei + 1):
            if (str[i] == '('):
                s.append(str[i])

            elif (str[i] == ')'):
                if (s[-1] == '('):
                    s.pop()
                    if (len(s) == 0):
                        return i;
        return -1;

    def str2tree(self, str):
        if len(str) == 0:
            return None

        return self.str2treeUtil(str, 0, len(str) - 1)

    def str2treeUtil(self, str, start, end):
        if start > end:
            return None

        root = TreeNode(int(str[start]))
        index = -1

        if (start + 1 <= end and str[start + 1] == '('):
            index = self.findIndex(str, start + 1, end)

        if index != -1:
            root.left = self.str2treeUtil(str, start + 2, index - 1)
            root.right = self.str2treeUtil(str, index + 2, end - 1)

        return root

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
        if (t is None):
            return None
        result.append(t.val)
        if (t.left is not None or t.right is not None):
            result.append("(")
            self.tree2strUtil(t.left, result)
            result.append(")")

        if (t.right is not None):
            result.append("(")
            self.tree2strUtil(t.right, result)
            result.append(")")



root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)

s=Solution()
print s.tree2str(root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
print s.tree2str(root)

root3 = s.str2tree("1(2()(4))(3)")
print "Calling"
#root3.inorderTraversal()
