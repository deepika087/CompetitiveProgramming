__author__ = 'deepika'


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Solution:

    count = 0
    def __init__(self, arr):
        self.arr = arr
        self.root = None

    def convertToTree(self):

        left = 0
        right = len(self.arr) - 1

        t = self.convertToTreeUtil(left, right)
        self.PrintInOrder(t)

    def PrintInOrder(self, root):

        if root != None:
            self.PrintInOrder(root.left)
            print(root.data)
            self.PrintInOrder(root.right)

    def minInArray(self, left, right):
        if left == right:
            return left

        if right == left + 1:
            if self.arr[right] < self.arr[left]:
                return right
            return left

        minIndex = left
        for i in range(left+1, right+1):
            if self.arr[i] < self.arr[minIndex]:
                minIndex = i
        return minIndex

    def convertToTreeUtil(self, left, right):

        if left > right or right < 0 or left >= len(self.arr):
            return None

        minIndex = self.minInArray(left, right)

        root = Node(self.arr[minIndex])

        root.left = self.convertToTreeUtil(left, minIndex-1)
        root.right = self.convertToTreeUtil(minIndex+1, right)

        return root



s=Solution([5, 3, 7, 4, 1, 2 ,6])
s.convertToTree()
