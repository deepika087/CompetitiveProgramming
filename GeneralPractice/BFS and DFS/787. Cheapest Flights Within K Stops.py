__author__ = 'deepika'

"""
Runtime: 136 ms, faster than 36.02% of Python online submissions for Cheapest Flights Within K Stops.
Memory Usage: 14.7 MB, less than 51.65% of Python online submissions for Cheapest Flights Within K Stops.
"""
import sys

class Solution(object):

    def dataRepresentation(self, flights):

        graph = dict()
        someSource = set()
        for flight in flights:
            someSource.add(flight[0])
            if flight[0] in graph:
                graph[flight[0]].append([flight[1], flight[2]])
            else:
                graph[flight[0]] = [ [flight[1], flight[2]] ]
        return graph, someSource

    def getNeighbours(self, popped, graph):
        if popped in graph:
            return graph[popped]
        return []

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        graph, someSource = self.dataRepresentation(flights)

        queue = []
        seen = dict()
        queue.append( [ src, 0] )
        seen[src] = 0

        dist = 0

        minCost = sys.maxint
        while len(queue) > 0:
            nextLevel = []

            while len(queue) > 0:
                popped = queue.pop(0)

                if dist > K:
                    continue

                neighbours = self.getNeighbours(popped[0], graph)
                if len(neighbours) > 0:
                    for neighbour in neighbours:
                        if neighbour[0] in seen and seen[neighbour[0]] <= popped[1] + neighbour[1]:
                            continue

                        if neighbour[0] == dst:
                            minCost = min(minCost, popped[1] + neighbour[1])
                            continue

                        nextLevel.append([ neighbour[0], popped[1] + neighbour[1] ])
                """
                This is a unique case because seen is not only important. it is important it was seen with a greater weight.
                This time if we see the same node with the lesser weight we still have to traverse it.
                """
                if popped[0] not in seen:
                    seen[popped[0]] =  [popped[1]] # THIS LINE IS IMPORTANT HERE
                else:
                    seen[popped[0]] = min(seen[popped[0]], popped[1])

            queue = nextLevel
            dist += 1

        return minCost if minCost != sys.maxint else -1


s=Solution()
print(s.findCheapestPrice(
    5, [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]], 0, 4, 3)) #40
print(s.findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0, 2, 2))  #7
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0)) #500
print(s.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1)) #200
print(s.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)) #-1
print(s.findCheapestPrice(8, [[3,4,7],[6,2,2],[0,2,7],[0,1,2],[1,7,8],[4,5,2],[0,3,2],[7,0,6],[3,2,7],[1,3,10],[1,5,1],[4,1,6],[4,7,5],[5,7,10]],
 4, 3, 7)) #13
