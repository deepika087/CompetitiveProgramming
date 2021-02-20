__author__ = 'deepika'

"""
This solution will take O(max( r1, r2))
Space = O(height of r1 ) + O(height of r2)

There is no way given the value of r1.val we find where the max common element might be. Also, you don't have to stop at the first match.
In there might be further matches. So, the idea is do the inorder traversal and save only the left nodes. Then when you pop a left node, if it has right node
then recursively add the left nodes of this right node and compare till you exhaust all the element.

Don't stop at the first match. Infact the first match will be the smallest match possible.

"""
class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

    def __str__(self):
        return "{" + str(self.val) + "}"

    def __repr__(self):
        return self.__str__()

class Solution:

    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

        self.s1 = []
        self.s2 = []

        self.leftRecurse(r1, True)
        self.leftRecurse(r2, False)

    def leftRecurse(self, root, boolean): #Using the boolean to figure out the stack to which I need to append the node.

        stack = self.s1 if boolean else self.s2
        while root != None:
            stack.append(root)
            root = root.left

    def findMaxCommmon(self):

        candidate = -float('inf')

        while self.s1 and self.s2:
            popped1 = self.s1.pop()
            popped2 = self.s2.pop()

            #print("Comparing: ", popped1.val, " ", popped2.val)
            if popped1.val < popped2.val:
                self.leftRecurse(popped1.right, True)
                self.s2.append(popped2)

            elif popped1.val > popped2.val:
                self.leftRecurse(popped2.right, False)
                self.s1.append(popped1)

            else:
                candidate = max(popped1.val, candidate)
                self.leftRecurse(popped1.right, True)
                self.leftRecurse(popped2.right, False)
        return candidate

r1 = Node(10)
r1.left = Node(5)
r1.right = Node(15)
r1.left.left = Node(1)
r1.right.left = Node(14)
r1.right.right = Node(20)
r1.right.right.right = Node(21)

r2 = Node(25)
r2.left = Node(21)
r2.right = Node(27)
r2.right.left = Node(26)
r2.right.right = Node(29)
r2.right.right.right = Node(31)

s1=Solution(r1, r2)
print(s1.findMaxCommmon())

s2=Solution(r1, r1)
print(s2.findMaxCommmon())

s3=Solution(r2, r2)
print(s3.findMaxCommmon())

s4=Solution(r2, r1)
print(s4.findMaxCommmon())

r1extended = r1
r1extended.right.right.right.right = Node(31)
s5=Solution(r2, r1extended)
print(s5.findMaxCommmon())

r3 = Node(3)
r3.left = Node(1)
r3.right = Node(4)

r4 = Node(4)
r4.left = Node(3)
r4.right = Node(5)

s6 = Solution(r3, r4)
print(s6.findMaxCommmon())

r3extended = Node(3)
r3extended.left = Node(1)
r3extended.right = Node(4)
r3extended.right.right = Node(5)

r4extended = Node(4)
r4extended.left = Node(3)
r4extended.right = Node(5)
s7 = Solution(r3extended, r4extended)
print(s7.findMaxCommmon())
