__author__ = 'deepika'


class Node:

    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class GenericNode:

    def __init__(self, d):
        self.val = d
        self.children = []

    def __repr__(self):
        return str(self.val)

class Solution:

    def LCA(self, root, keyNodes):

        ancestors = []

        #Intially there is No Matching Nodes
        matchingNodes = 0;
        self.getKeysCount(root, keyNodes, ancestors);

        #First Node in the Ancestors list
        # is the Least Common Ancestor of
        # Given keyNodes
        return ancestors[0]

    def getKeysCount(self, root, keyNodes, ancestors):
        if root is None:
            return 0

        matchingNodes = 0
        matchingNodes += self.getKeysCount(root.left, keyNodes, ancestors) + self.getKeysCount(root.right, keyNodes, ancestors)

        if root.val in keyNodes:
            matchingNodes += 1

        if matchingNodes == len(keyNodes):
            print("Appending root: ", root.val, " to ancestors")
            ancestors.append(root)
        return matchingNodes

    def LCAGeneric(self, root, keyNodes):

        ancestors = []

        self.getKeysCountGeneric(root, keyNodes, ancestors);

        return ancestors[0]

    def getKeysCountGeneric(self, root, keyNodes, ancestors):
        if root is None:
            return 0

        matchingNodes = 0
        for node in root.children:
            matchingNodes += self.getKeysCountGeneric(node, keyNodes, ancestors)

        if root.val in keyNodes:
            matchingNodes += 1

        if matchingNodes == len(keyNodes):
            ancestors.append(root)
        return matchingNodes


t = Node(1)
t.left = Node(2)
t.right = Node(3)
t.left.left = Node(4)
t.left.right = Node(5)
t.right.left = Node(6)
t.right.right = Node(7)
t.left.left.left = Node(8)
t.left.left.right = Node(9)
t.left.right.left = Node(10)
t.left.right.right = Node(11)


s=Solution()
#print(s.LCA(t, [8, 9]))
#print(s.LCA(t, [8, 9, 10, 11]))
#print(s.LCA(t, [2, 1]))

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
r1.children = [r2, r3, r4]
r2.children = [r5, r6, r7]
r3.children = [r8, r9]
print(s.LCAGeneric(r1, [2, 3, 4]))
print(s.LCAGeneric(r1, [5, 6, 7]))
print(s.LCAGeneric(r1, [5, 6, 7, 9]))
