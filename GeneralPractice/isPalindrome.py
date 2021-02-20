__author__ = 'deepika'

import copy
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return "[" + str(self.val) + "]"

    def __repr__(self):
        return "[" + str(self.val) + "]"



class LinkList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

    def printList(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp)
            temp = temp.next

        print result

    def checkIfPalin(self):
        return self.checkIfPalinUtil(copy.copy(self.head))

    def checkIfPalinUtil(self, headDetached):

        if headDetached is None:
            return True

        res = self.checkIfPalinUtil(headDetached.next)
        if res == False:
            return False

        #if headDetached is not None and dontmove is not None:
        print "Comparing: ", self.head.val , " and ", headDetached.val
        result = self.head.val == headDetached.val

        self.head = self.head.next

        return result



myl = LinkList()
myl.insert(1)
myl.insert(2)
myl.insert(4)
#myl.insert(3)
myl.insert(2)
myl.insert(1)

myl.printList()

print "Pallindrome: ", myl.checkIfPalin()
