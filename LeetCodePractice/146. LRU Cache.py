__author__ = 'deepika'
"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 362 ms
"""
class Node(object):
    def __init__(self, _k, _v):
        self.key = _k
        self.val = _v
        self.next = None
        self.prev = None

    def __repr__(self):
        return "[" + str(self.key) + ", " + str(self.val) + "]"


class LRUCache(object):

    def display(self):
        temp = self.front
        while temp:
            print temp
            temp = temp.next

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.front = None
        self.rear = None
        self.capacity = capacity
        self.hashMap = dict()

    def moveToFront(self, node):
        if self.front == node:
            return

        if node.next is None: # if this is the last node
            self.rear = node.prev
            self.rear.next = None

            self.front.prev = node
            node.next = self.front
            node.prev = None # sanitize the node
        else: # Node was somewhere in middle of the, rear will remain the same
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            node.prev = None
            node.next = self.front
            self.front.prev = node
        self.front = node

    def insertAtFront(self, new_node):
        self.front.prev = new_node
        new_node.next = self.front
        self.front = new_node

    def removeRearNode(self):
        key_to_return = self.rear.key
        if self.rear == self.front: #only one node
            self.rear = None
            self.front = None
        else:
            self.rear.prev.next = None
            self.rear = self.rear.prev
        return key_to_return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashMap:
            required_node = self.hashMap[key]
            to_return = required_node.val
            #print "Atleast seletec the value to return : ", to_return
            self.moveToFront(required_node)
            return to_return
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashMap:
            self.hashMap[key].val = value #Update value
            self.moveToFront(self.hashMap[key])
            return

        if self.capacity > 0:
            new_node = Node(key, value)
            self.hashMap[key] = new_node
            self.capacity = self.capacity - 1
            if self.front == None:
                self.front = new_node
                self.rear = new_node
            else:
                self.insertAtFront(new_node)
        else: #capacity is zero
            keyRemove = self.removeRearNode()
            del self.hashMap[keyRemove]
            self.capacity = self.capacity + 1
            self.put(key, value)

# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,10)
obj.put(2,20)
obj.display()
print "Value for key 1: ", obj.get(1)
obj.display()
obj.put(3,30)
print "After put"
obj.display()
print "Value for key 2: ", obj.get(2)
