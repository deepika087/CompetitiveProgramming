__author__ = 'deepika'
# A complete working Python program to find n'th node
# in a linked list

# Node class
import copy
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

    def printList(self):
        head = self
        result = ""
        while(head is not None):
            result += str(head.data) + " --> "
            head = head.next
        result += "None"
        return result

    def getNthRecurse(self, index):
        if (index == 0):
            return self.data
        return self.next.getNthRecurse(index-1)

    def isPalindrom(self):
        return self.isPalinUtil(copy.copy(self))


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None


    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Returns data at given index in linked list
    def getNth(self, index):
        current = self.head # Initialise temp
        count = 0 # Index of current node

        # Loop while end of linked list is not reached
        while (current):
            if (count == index):
                return current.data
            count += 1
            current = current.next

        # if we get to this line, the caller was asking
        # for a non-existent element so we assert fail
        #assert(false)
        return 0;

    def getNthRecurse(self, index):
        print self.head.__class__.__name__

# Code execution starts here
if __name__=='__main__':

    llist = Node(1)
    llist.next = Node(2)
    llist.next.next= Node(3);
    llist.next.next.next= Node(2);
    llist.next.next.next.next = Node(1);
    #llist.next.next.next.next.next = Node(6);

    print " The list looks like : ", llist.printList()
    # actually print n+1 element assuming 0 based indexing.
    n = 3
    print ("Element at index 3 is :", llist.getNthRecurse(n))

    print " check if list is pallindrome or not: ", llist.isPalindrom()