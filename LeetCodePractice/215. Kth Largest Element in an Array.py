__author__ = 'deepika'

"""
31 / 31 test cases passed.
Status: Accepted
Runtime: 82 ms

50%
"""
import copy
class Heap:
    def __init__(self, inv):
        self.size = len(inv)
        self.heap = copy.copy(inv)

    def build_heap(self):
        for i in range(self.size/2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        greatest = i
        if l < self.size and self.heap[l] > self.heap[i]:
            greatest = l
        if r < self.size and self.heap[r] > self.heap[greatest]:
            greatest = r
        if greatest != i:
            self.heap[i], self.heap[greatest] = self.heap[greatest], self.heap[i]
            self.heapify(greatest)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def maxOfHeap(self):
        return self.heap[0]

    def addAndHeapify(self, num):
        self.heap[0] = num
        self.heapify(0)

    def deleteAndHeapify(self):
        maxNum = self.heap[0]
        if maxNum == 1:
            self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0] - 1
            self.size -= 1
            self.heapify(0)
        else:
            self.heap[0] -= 1
            if self.size < 3:
                self.heapify(0)
            elif self.size > 2 and self.heap[0] <= min(self.heap[1], self.heap[2]):
                self.heapify(0)
        return maxNum

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(inventory) == 0:
            return 0
        if len(inventory) == 1:
            return (orders * (orders + 1)/2) % (10**9 + 7)

        h = Heap(inventory)
        h.build_heap()

        result = 0

        while orders > 0:
            num = h.deleteAndHeapify()
            #print("picking: ", num)
            result += num ;
            result = result % (10**9 + 7)
            orders -= 1

        return result

s=Solution()
assert s.maxProfit(inventory = [2,5], orders = 4) == 14
assert s.maxProfit([3,5], orders = 6) == 19
assert s.maxProfit([2, 8, 4, 10, 6], orders = 20) == 110
print s.maxProfit([1000000000], orders = 1000000000)


