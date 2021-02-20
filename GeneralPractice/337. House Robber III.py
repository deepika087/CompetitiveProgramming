__author__ = 'deepika'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
My approach assumes that there must be incl, excl strict order.
consider a left only tree 4 -> 1 -> 2 -> 3  Here the asnwer is 7. so you skip 1, 2
"""
class Solution(object):

    def rob1(self, root):
        def maxgain(node=root):
            if not node: return 0, 0

            left_inc, left_exc = maxgain(node.left)
            right_inc, right_exc = maxgain(node.right)

            return node.val + left_exc + right_exc, max(left_inc, left_exc) + max(right_inc, right_exc)

        return max(maxgain())



    def rob(self, root):

        def maxGain(node=root):

            if node is None:
                return 0, 0

            left_inc, left_excl = maxGain(node.left)
            right_inc, right_excl = maxGain(node.right)

            return node.val + left_excl + right_excl, max(left_excl, left_inc) + max(right_excl, right_inc)
        return max(maxGain())


    def robNotworking(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        parentTaken = False
        self.valueWithOutParent = 0
        self.valueWithParent = 0
        self.robUtil(root, parentTaken )
        return max(self.valueWithParent, self.valueWithOutParent)

    def robUtil(self, root, parentTaken):
        #print("Begiining, " + str(parentTaken))
        if root is None:
            return self.valueWithParent, self.valueWithOutParent

        if parentTaken:
            self.valueWithOutParent += root.val
        else:
            self.valueWithParent += root.val

        #print(self.valueWithOutParent, self.valueWithParent)
        self.robUtil(root.left, False if parentTaken else True)
        self.robUtil(root.right, False if parentTaken else True)

s=Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)



root2 = TreeNode(3)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left =  TreeNode(3)
root2.left.right = TreeNode(1)


root3 = TreeNode(3)
root3.left = TreeNode(4)
root3.right = TreeNode(5)
root3.left.left =  TreeNode(1)
root3.left.right = TreeNode(3)
root3.right.left = TreeNode(1)

print(s.rob(root1))
#print(s.rob(root2))
#print(s.rob(root3))