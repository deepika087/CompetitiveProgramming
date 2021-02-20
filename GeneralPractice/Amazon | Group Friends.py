__author__ = 'deepika'


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = val
        self.rank = 0

class Solution:

    def __init__(self):
        self.collection = dict()

    def addfriend(self, f1, f2):

        fNode1 = None
        fNode2 = None
        if f1 not in self.collection:
            fNode1 = Node(f1)
            self.collection[f1] = fNode1
        else:
            fNode1 = self.collection[f1]

        if f2 not in self.collection:
            fNode2 = Node(f2)
            self.collection[f2] = fNode2
        else:
            fNode2 = self.collection[f2]

        if fNode1.rank == fNode2.rank:
            fNode1.rank += 1
            fNode2.parent = fNode1.val
        elif fNode1.rank > fNode2.rank:
            fNode2.parent = fNode1.val
        else:
            fNode1.parent = fNode2.val


    def find(self, f):
        if f not in self.collection:
            return None

        while self.collection[f].parent != f:
            return self.find(self.collection[f].parent)
        return self.collection[f].parent

    def findFriendShip(self, f1, f2):
        if f1 not in self.collection or f2 not in self.collection:
            return False

        fNode1 = self.find(f1)
        fNode2 = self.find(f2)

        return self.collection[fNode1].parent == self.collection[fNode2].parent

s=Solution()
s.addfriend(1, 2)
s.addfriend(2, 3)
s.addfriend(3, 4)
s.addfriend(5, 6)
assert s.findFriendShip(1, 4) == True
assert s.findFriendShip(2, 3) == True
assert s.findFriendShip(1, 5) == False