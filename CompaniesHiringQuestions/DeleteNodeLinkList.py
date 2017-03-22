# Python program to delete a node in a linked list
# at a given position
 
# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteUtil(self, target):

        while(self.head.data > target):
            self.head = self.head.next

        ptr = self.head # first elemnt < target
        prev = ptr
        ptr = ptr.next
        #print " Before ptr ->", ptr.data, " prev ->" , prev.data
        while(ptr):
            if (ptr.data > target):
                print " Eval " + ptr.data
                prev.next = ptr.next
            else:
                prev = ptr
                ptr = ptr.next


    def printList(self):
        temp = self.head
        while(temp):
            print " %d " %(temp.data),
            temp = temp.next

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
print " Before "
llist.printList()
llist.deleteUtil(3)
print " After "
llist.printList()