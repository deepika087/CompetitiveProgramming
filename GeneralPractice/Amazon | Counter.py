__author__ = 'deepika'

# Assumptions:
#   1. Timestamps will always come in strictly non-decreasing order.
#   2. Same timestamp can be hit multiple times.
# Approach: use a linked list to save ts, number of ts hit was sent for that ts.
class Node:
    def __init__(self, d):
        self.ts = d
        self.count = 1
        self.next = None

class Solution:

    def __init__(self):
        self.start = None
        self.tail = None
        self.count_so_far = 0
        #self.ts_to_Node = dict()

    def getCount(self):
        print("Returning: ", self.count_so_far)
        return self.count_so_far

    def hit(self, ts): #this implmentation is O(n) time.

        while self.start and (ts - self.start.ts) >= 3600:
            self.count_so_far -= self.start.count
            self.start = self.start.next

        # Cz at a time one entry will be appended
        self.count_so_far += 1
        if self.start is None:
            n = Node(ts)
            self.start = self.tail = n
            return
        if self.tail.ts == ts:
            self.tail.count += 1
            return

        self.tail.next = Node(ts)
        self.tail = self.tail.next


class HitCounterConstantTime:

    def __init__(self):
        self.hits = [0] * 3600
        self.timestamp = [0] * 3600
        self.latest_timestamp = 0

    def hit(self, ts):

        self.latest_timestamp = ts
        effective_ts = ts%3600
        if self.timestamp[effective_ts] != ts:
            self.timestamp[effective_ts] = ts
            self.hits[effective_ts] = 1
        else:
            self.hits[effective_ts] += 1

    def getCount(self):

        result = 0
        for i in range(3600):

            if self.latest_timestamp - self.timestamp[i] <= 3600:
                result += self.hits[i]

        return result
#s=Solution()
s = HitCounterConstantTime()
s.hit(1)
s.hit(1)
assert s.getCount() == 2
s.hit(2)
s.hit(2)
assert s.getCount() == 4
s.hit(3)
s.hit(3)
assert s.getCount() == 6
s.hit(3599)
assert s.getCount() == 7
s.hit(3600)
assert s.getCount() == 8
s.hit(3601)
assert s.getCount() == 7
s.hit(3602)
s.hit(3603)
s.hit(3604)
assert s.getCount() == 6
s.hit(3700)
assert s.getCount() == 7