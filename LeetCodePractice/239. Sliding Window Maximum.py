__author__ = 'deepika'

"""
18 / 18 test cases passed.
Status: Accepted
Runtime: 295 ms
"""
class Myqueue(object):
    def __init__(self):
        self.arr = []

    def push_back(self, item):
        self.arr.append(item)

    def pop_front(self):
        return self.arr.pop(0)

    def pop_back(self):
        return self.arr.pop(-1)

    def peek_front(self):
        #print self.arr
        return self.arr[0]

    def peek_back(self):
        return self.arr[-1]

    def isempty(self):
        return len(self.arr) == 0

    def __repr__(self):
        return ", ".join(map(lambda x: str(x), self.arr))

class Solution(object):
    def maxSlidingWindow(self, arr, k):

        Q = Myqueue()
        result = []
        for i in range(0, k):

            #print " For i : ", i, "Q.peek_back() : ", Q.peek_back() if not Q.isempty() else None
            while (not Q.isempty() and arr[i] >= arr[Q.peek_back()]):
                Q.pop_back()

            Q.push_back(i)

        for i in range(k, len(arr)):
            result.append(arr[Q.peek_front()])

            while (not Q.isempty() and Q.peek_front() <= i - k):
                Q.pop_front()

            while (not Q.isempty() and arr[i] >= arr[Q.peek_back()]):
                Q.pop_back()
            Q.push_back(i)

        result.append(arr[Q.peek_front()])
        return result

s=Solution()
print s.maxSlidingWindow([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)

print s.maxSlidingWindow([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4)
