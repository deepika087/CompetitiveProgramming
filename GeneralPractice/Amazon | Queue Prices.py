__author__ = 'deepika'


"""
We have two Queues where each queue contains timestamp price pair. We have to return list of list[[price1, price 2]] for all those timestamps where abs(ts1-ts2) <= 1 second where ts1 and price1 are the from the first queue and ts2 and price2 are from the second queue.

Follow up:- one queue is slow

"""

# Approach: Idea is that keep a min-heap of timestamps. Till the time you find ts difference lte 1, keep popping the smaller timestamp.
# If you find equal timestamps, test the next neighbour candidates as well. The approach assumes no duplicates in terms of timestamp.
# Time: O(n log n ), n = min(number of pairs in list1, number of pairs in list2)
import heapq
class Solution:

    def findPairs(self, list1, list2):

        pq1 = []
        pq2 = []

        for pair in list1:
            heapq.heappush(pq1, pair)

        for pair in list2:
            heapq.heappush(pq2, pair)

        while pq1 and pq2:

            if abs(pq1[0][0] - pq2[0][0]) > 1:
                if pq1[0][0] < pq2[0][0]:
                    heapq.heappop(pq1)
                else:
                    heapq.heappop(pq2)
            else:
                print(pq1[0], pq2[0])
                if pq1[0][0] < pq2[0][0]:
                    heapq.heappop(pq1)
                elif pq2[0][0] < pq1[0][0]:
                    heapq.heappop(pq2)
                else:
                    if len(pq2) >= 2 and abs(pq1[0][0] - pq2[1][0]) <= 1:
                        print(pq1[0], pq2[1])
                    if len(pq1) >= 2 and abs(pq1[1][0] - pq2[0][0]) <= 1:
                        print(pq1[1], pq2[0])
                    heapq.heappop(pq1)
                    heapq.heappop(pq2)


s=Solution()
list1 = [

    [1, 10],
    [2, 20],
    [3, 30],
    [10, 100],
    [11, 110]
]

list2 = [

    [9, 90],
    [10, 1],
    [11, 111]
]

list3 = [

    [1, 1],
    [2, 2],
    [3, 3]
]
s.findPairs(list1, list2)
s.findPairs(list3, list3)
