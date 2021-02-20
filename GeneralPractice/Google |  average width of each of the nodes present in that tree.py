__author__ = 'deepika'



class Node:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None

class GenericNode:

    def __init__(self, d):
        self.val = d
        self.children = []

class Solution:

    def findAverageWidth(self, binaryTree):

        if binaryTree == None:
            return 0, 0

        num_of_nodes_left, level_on_left = self.findAverageWidth(binaryTree.left)
        num_of_nodes_right, level_on_right = self.findAverageWidth(binaryTree.right)

        effectiveNodes = num_of_nodes_left + num_of_nodes_right + 1
        effectiveLevels = max(level_on_right, level_on_left) + 1

        print(str(binaryTree.val) + " ---> " + str ( effectiveNodes * 1.0 / effectiveLevels ))

        return effectiveNodes, effectiveLevels

    def findAverageWidthNAryTree(self, tree):
        if tree == None:
            return [0, 0]

        num_of_nodes = 0
        num_of_levels = 0

        for node in tree.children:
            n, l = self.findAverageWidthNAryTree(node)
            num_of_nodes += n
            num_of_levels = max(num_of_levels, l)

        num_of_nodes += 1
        num_of_levels += 1

        print(str(tree.val) + " ---> " + str ( num_of_nodes * 1.0 / num_of_levels ))
        return num_of_nodes, num_of_levels


t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)

s=Solution()
s.findAverageWidth(t)
t.left.left.left = Node(8)
t.left.left.right = Node(9)
print("----------------------")
s.findAverageWidth(t)

print("N-Ary Tree Output")
r1 = GenericNode(1)
r2 = GenericNode(2)
r3 = GenericNode(3)
r4 = GenericNode(4)
r5 = GenericNode(5)
r6 = GenericNode(6)
r7 = GenericNode(7)
r8 = GenericNode(8)
r9 = GenericNode(9)
r1.children = [r2, r3]
r2.children = [r4, r5]
r3.children = [r6, r7]
r4.children = [r8, r9]
s.findAverageWidthNAryTree(r1)
