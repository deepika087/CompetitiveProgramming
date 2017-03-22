
# Definition for a binary tree node.
"""
109 / 109 test cases passed.
Status: Accepted
Runtime: 82 ms

functional Approach
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    """
    To move the value up
    """
    def sumNumbersUtilUp(self, root):
        if (root is None):
            return 0

        max_so_far=0
        max_so_far = max_so_far + self.sumNumbersUtil(root.left)
        max_so_far = max_so_far + self.sumNumbersUtil(root.right)

        print str(root.val) +  "+" +  str(max_so_far)
        return root.val + max_so_far

    """
    To move value down

    """
    def sumNumbersUtil(self, root, max_so_far, total):

        if (root is None):
            return total

        total = self.sumNumbersUtil(root.left, str(root.val) + str(max_so_far), total)
        total = self.sumNumbersUtil(root.right, str(root.val) + str(max_so_far), total)
        if (root.left is None and root.right is None):
            temp=(str(root.val) + max_so_far)[::-1]
            total += int(temp)
        return total

    """
        Print all paths.
        209 / 209 test cases passed.
        Status: Accepted
        Runtime: 59 ms
    """
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root is None):
            return 0

        total = 0
        max_so_far=""
        return self.sumNumbersUtil(root, max_so_far, total)

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
        if (result[0][0:2] == "->"):
            return list(result[0][2:])
        else:
            return result

s=Solution()
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.left=TreeNode(4)
t.left.right=TreeNode(5)
t.left.right=TreeNode(5)
t.right.left=TreeNode(6)
t.right.right=TreeNode(7)
t.left.left.left=TreeNode(8)
t.left.left.right=TreeNode(9)



#print s.sumNumbers(t)

print s.binaryTreePaths(t)