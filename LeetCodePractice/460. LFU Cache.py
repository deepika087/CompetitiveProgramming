__author__ = 'deepika'

class Node(object):
    def __init__(self, _k, _v):
        self.key = _k
        self.val = _v
        self.next = None
        self.prev = None
        self.freq = 1

    def __repr__(self):
        return "[" + str(self.key) + ", " + str(self.val) + "]"

    def __cmp__(self, other):
        return cmp(other.freq, self.freq)

class LFUCache(object):

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

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashMap:
            required_node = self.hashMap[key]
            required_node.freq = required_node.freq + 1
            to_return = required_node.val
            self.moveToFront(required_node)
            return to_return
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)