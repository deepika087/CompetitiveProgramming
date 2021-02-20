__author__ = 'deepika'
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    """
    To send the values downwards
    """
    def sumEntireTreeUtil(self, root, sumTotal):
        if (root is None):
            return sumTotal

        sumTotal += root.val
        sumTotal = self.sumEntireTreeUtil(root.left, sumTotal)
        sumTotal = self.sumEntireTreeUtil(root.right, sumTotal)
        return sumTotal

    def sumEntireTreeDownwards(self, root):
        sumTotal = 0
        sumTotal = self.sumEntireTreeUtil(root, sumTotal)
        return sumTotal

    ####################
    ## Get sum from children: Move value up
    ####################
    def isLeaf(self, root):
        return root.left is None and root.right is None

    def getSumFromChildren(self, root):
        if root is None:
            return 0

        leftSum = self.getSumFromChildren(root.left)
        rightSum = self.getSumFromChildren(root.right)

        if (self.isLeaf(root)):
            return root.val
        return leftSum + rightSum + root.val

    ########
    # This is a look ahead version to compute total sum of binary tree
    ########
    def getValue(self, root):
        if root is None:
            return 0
        return root.val

    def getSumLookAheadUtil(self, root, sumTotal):
        if root is None:
            return sumTotal

        sumTotal += self.getValue(root.left) + self.getValue(root.right)
        sumTotal = self.getSumLookAheadUtil(root.left, sumTotal)
        sumTotal = self.getSumLookAheadUtil(root.right, sumTotal)
        return  sumTotal

    def getSumLookAhead(self, root):
        sumTotal = self.getValue(root) #Otherwise the root itself will miss out.
        sumTotal = self.getSumLookAheadUtil(root, sumTotal)
        return sumTotal

s=Solution()
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.left=TreeNode(4)
t.left.right=TreeNode(5)
t.right.left=TreeNode(6)
t.right.right=TreeNode(7)
t.left.left.left=TreeNode(8)
t.left.left.right=TreeNode(9)

print s.sumEntireTreeDownwards(t)
print s.getSumFromChildren(t)
print s.getSumLookAhead(t)