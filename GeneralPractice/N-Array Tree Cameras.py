__author__ = 'deepika'

"""
Extension of binary tree camera coverage.
BAsically this code can also be used to figure out that hwo many ful fillment center are required.

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = dict()

class Solution(object):
    ans = 0
    covered = {None}

    def minFulFillmentCenters(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.minFulFillmentCentersUtil(root, None)
        return self.ans

    def minFulFillmentCentersUtil(self, root, par):

        if root:

            for c in root.children:
                self.minFulFillmentCentersUtil(root.children[c], root)

            if par is None and root not in self.covered or \
                any(root.children[c] not in self.covered for c in root.children):
                self.ans += 1
                #print("Adding root: ", root.val)
                self.covered.update({root, par})
                self.covered.update( { c for c in root.children})


T1=TreeNode(1)
T1.children[2] = TreeNode(2)
T1.children[3] = TreeNode(3)
T1.children[4] = TreeNode(4)
T1.children[2].children[5] = TreeNode(5)
T1.children[2].children[6] = TreeNode(6)
T1.children[3].children[7] = TreeNode(7)
T1.children[4].children[8] = TreeNode(8)
T1.children[4].children[8].children[9] = TreeNode(9)
s=Solution()
print(s.minFulFillmentCenters(T1))

