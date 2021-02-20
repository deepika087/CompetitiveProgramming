__author__ = 'deepika'

"""
The interviewer her self was confused. She was confused between time and size of the window.

Well anyway the idea was that you have an infinite long stack and you have to put and get and get average.
But you have to remove old entries side by side.

Mostly like least recently used stuff only. I used a comvo of doubly linked list and a hashmap.
"""
import datetime

# using now() to get current time

class Node:
    def __init__(self, key, value, ts):
        self.key = key
        self.value = value
        self.ts = ts
        self.prev = None
        self.next = None

    def __repr__(self):
        return "[ key: " + self.key + " value : " + str(self.value) + " ts: " + str(self.ts) + "]"

class WindowedMap:
    def __init__(self, window_size): #Assume Millisec as of now
        self.window_size = window_size
        self.head = None
        self.tails = None
        self.global_sum = 0
        self.mapping = dict()

    def _print(self):
        print("current length : ", len(self.mapping.keys()))

        start = self.head
        while start is not None:
            print(start)
            start = start.next


    # Puts or replaces a previous key value pairing
    def _prune(self, current_time):
        while self.head and current_time.microsecond - self.head.ts > self.window_size:
            temp_key = self.head.key
            self.global_sum -= self.head.value
            del self.mapping[temp_key]
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def put(self, key, value):
        current_time = datetime.datetime.now()

        # 1.) First prune the link list
        self._prune(current_time)

        # 2.) Append at the end basically modify self.tail
        if key not in self.mapping:
            insert_node = Node(key, value, current_time.microsecond)

            if self.head is None:
                self.head = self.tail = insert_node
            else:
                self.tail.next = insert_node
                insert_node.prev = self.tail
                self.tail = self.tail.next
            self.mapping[key] = insert_node
        else:

            to_update_node = self.mapping[key]
            self.global_sum -= to_update_node.value

            to_update_node.value = value
            to_update_node.ts = current_time.microsecond

            to_update_node.prev.next = to_update_node.next
            to_update_node.next.prev = to_update_node.prev

            self.tail.next = to_update_node
            to_update_node.prev = self.tail
            self.tail = self.tail.next

        self.global_sum += value



    # Gets the most recent value for the key
    def get(self, key):
        current_time = datetime.datetime.now()

        # 1.) First prune the link list
        self._prune(current_time)

        # 2.) Now check if mapping exists
        if key in self.mapping:
            return self.mapping[key].value
        return None

    # Gets the average for all values inside the window
    def getAverage(self):
        current_time = datetime.datetime.now()

        # 1.) First prune the link list
        self._prune(current_time)

        if len(self.mapping.keys()) == 0:
               return 0.0
        return self.global_sum * 1.0 / len(self.mapping.keys())

w=WindowedMap(10)
w.put("foo", 2)
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
print("average: " + str(w.getAverage()))
w.put("bar", 3)
w.put("cbar", 10)
print("average: " + str(w.getAverage()))
#w._print()
print(w.get("cbar"))
print("average: " + str(w.getAverage()))
print(w.get("cbar"))
print(w.get("cbar"))
print(w.get("cbar"))
print(w.get("cbar"))
print(w.get("cbar"))
print(w.get("cbar"))
print("average: " + str(w.getAverage()))

"""

current_time = datetime.datetime.now()
print(current_time)

1, 2, 3 <- size = 5

window size = 1000

put("foo", 5) t 1000
put("bar", 10) t 1010

getAvg() -> 7.5 t 1050

getAvg() -> 10 t 2005

-> if data is well in time limit then put
-> if data is beyond the time limit then first prune values -> put
"""