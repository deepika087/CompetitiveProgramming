__author__ = 'deepika'

"""
This code will return iterator for inorder traversal of a BST
"""
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         return str(self.val)

class InorderIterator:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.appendLeftTree()

    def appendLeftTree(self, start=None):
        temp = self.root if start is None else start
        while temp:
            self.stack.append(temp)
            temp = temp.left


    def next(self):
        if self.stack:
            next_item = self.stack.pop()
            if next_item.right:
                self.appendLeftTree(next_item.right)
            return next_item.val
        return None

class ReverseInOrderIterator:

    def __init__(self, root):
        self.root = root
        self.stack = []
        self.appendRightTree()

    def appendRightTree(self, start=None):
        temp = self.root if start is None else start
        while temp:
            self.stack.append(temp)
            temp = temp.right


    def next(self):
        if self.stack:
            next_item = self.stack.pop()
            if next_item.left:
                self.appendRightTree(next_item.left)
            return next_item.val
        return None

class Solution:

    def binarySearchBST(self, root, key):
        left_itr = InorderIterator(root)
        right_itr = ReverseInOrderIterator(root)
        left_val = left_itr.next()
        right_val = right_itr.next()
        while True:
            if left_val >= right_val:
                break
            if left_val + right_val == key:
                print " Found: ", left_val, " ", right_val
            if left_val + right_val < key:
                left_val = left_itr.next()
            else:
                right_val = right_itr.next()

root=TreeNode(10)
root.left=TreeNode(5)
root.right=TreeNode(11)
root.left.left=TreeNode(1)
root.left.right=TreeNode(8)
root.left.right.left=TreeNode(7)
root.right.right=TreeNode(14)
itr = InorderIterator(root)
result = []
for i in range(7):
    result.append(itr.next())
print result

result = []
itr = ReverseInOrderIterator(root)
for i in range(7):
    result.append(itr.next())
print result

s=Solution()
s.binarySearchBST(root, 18)
