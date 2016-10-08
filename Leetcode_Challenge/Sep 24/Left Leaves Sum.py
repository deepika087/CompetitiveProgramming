
"""
Accepted soution
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if ( root is None):
            return 0
        sum = 0;
        if (root.left is not None and root.left.left is None and root.left.right is None):
            #print "found Leaf" , root.left.val
            sum = sum + root.left.val
        sumL = self.sumOfLeftLeaves(root.left)
        sumR = self.sumOfLeftLeaves(root.right)
        return sum + sumL + sumR

if __name__ == "__main__":
    sol =  Solution()
