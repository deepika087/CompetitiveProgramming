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

    # def __cmp__(self, other):
    #    return cmp(other.freq, self.freq)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.front = None
        self.rear = None
        self.capacity = capacity
        self.currentNodes = 0
        self.hashMap = dict()

    def moveToFront(self, node):
        if self.front == node:
            return

        if self.rear == node: # if this is the last node
            #print("1000")
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

    def putInFront(self, newNode):
        if self.front is None:
            self.front = newNode
            self.rear = newNode
        else:
            newNode.next = self.front
            self.front.prev = newNode
            self.front = newNode # rear remains as it is

    def printCache(self):
        #return
        start = self.front
        result = []
        while start is not None:
            result.append(start.key)
            start = start.next
        print("List so far",  ' '.join(str(result)))


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashMap:
            return -1

        required_node = self.hashMap[key]
        required_node.freq = required_node.freq + 1
        to_return = required_node.val
        #print("value to return", to_return)
        self.moveToFront(required_node) # the most recently used will be on the head of the linked list
        self.printCache()
        return to_return

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashMap:
            newNode = self.hashMap[key]
            newNode.val = value
            newNode.freq += 1
            self.moveToFront(newNode)
            return

        newNode = Node(key, value)
        if len(self.hashMap.keys()) == self.capacity: #evict but capacity remains the same.
            #print("reaching here")
            keyToremove = self.rear.key
            newLastNode = self.rear.prev
            #print("newLastNode ", newLastNode.val)
            newLastNode.next = None
            self.rear.next = Node
            self.rear.prev = Node
            self.rear = newLastNode
            #print("Deleting key", keyToremove)
            del self.hashMap[keyToremove]

        self.hashMap[key] = newNode
        self.putInFront(newNode)
        self.printCache()
        #print(self.hashMap)


# Your LFUCache object will be instantiated and called as such:
cache = LFUCache( 2  );

print("Test case 1")
cache.put(1, 1);
cache.put(2, 2);
print(cache.get(1))       # return 1
cache.put(3, 3);           # evict key 2
print(cache.get(2))       # returns -1 (not found)
print(cache.get(3))      # returns 3.
cache.put(4, 4);    # evicts key 1.
print(cache.get(1))      # returns -1 (not found)
print(cache.get(3))       # returns 3
print(cache.get(4))     # returns 4

print("Test Case 2")
cache2=LFUCache(3)
cache2.put(2,2)
cache2.put(1,1)
print(cache2.get(2))
print(cache2.get(1))
print(cache2.get(2))
cache2.put(3,3)
cache2.put(4,4)
print(cache2.get(3)) # -1
print(cache2.get(2)) # 2
print(cache2.get(1)) # 1
print(cache2.get(4)) # 4