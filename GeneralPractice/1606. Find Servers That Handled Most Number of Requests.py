__author__ = 'deepika'


"""
It is one of those problems in which data structue definition is more challenging than the actual code.
Time complexity : O(n log k)
"""
import heapq

class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """

        avail = list(range(k))
        count = [0]*k

        pq = []
        for i, a in enumerate(arrival):
            while pq and pq[0][0]  <= a:
                _, x = heapq.heappop(pq)
                heapq.heappush(avail, i + (x-i)%k)
            if avail:
                poppedServer = heapq.heappop(avail) % k
                heapq.heappush(pq, (a + load[i], poppedServer))
                count[poppedServer] += 1
        max_count = max(count)
        return [i for i in range(k) if count[i] == max_count] # this is important. Finding max again and again will increase the time complexity of this problem.


s=Solution()
print(s.busiestServers(k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] ))

