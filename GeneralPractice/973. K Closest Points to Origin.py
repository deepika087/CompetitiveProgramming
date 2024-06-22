"""
Accepted
600 ms
Beats 48.88%
"""
import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        k_points = []
        for point in points:
            incoming_dist = point[0] * point[0] + point[1] * point[1]

            if len(k_points) < k:
                heapq.heappush(k_points, (-incoming_dist, point[0], point[1]))
            else:
                temp_pop = heapq.heappop(k_points)
                if incoming_dist > -temp_pop[0]:
                    heapq.heappush(k_points, temp_pop)
                else:
                    heapq.heappush(k_points, (-incoming_dist, point[0], point[1]))

        result = []
        while k_points:
            popped = heapq.heappop(k_points)
            result.append([popped[1], popped[2]])
        return result

s=Solution()
print(s.kClosest(points = [[1,3],[-2,2]], k = 1))
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))