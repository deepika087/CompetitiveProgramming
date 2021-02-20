__author__ = 'deepika'

"""
Details
Runtime: 2716 ms, faster than 8.18% of Python online submissions for Maximal Network Rank.
Memory Usage: 15.3 MB, less than 20.30% of Python online submissions for Maximal Network Rank.
"""
class Solution(object):
    def representation(self, n, roads):
        dict = {}
        count = 1
        for road in roads:
            if road[0] not in dict:
                dict[road[0]] = []
            dict[road[0]].append( [road[1], count] )
            if road[1] not in dict:
                dict[road[1]] = []
            dict[road[1]].append( [road[0], count])
            count += 1
        return dict

    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        if len(roads) == 0:
            return 0
        #if len(roads) == 1:
        #    return 1
        data = self.representation(n, roads)

        maxL = 0
        print(data)

        for i in range(0, n):
            for j in range(i+1, n):
                #print("For pair", i, " and ", j)
                result = set()
                if i in data and j in data:
                    result.update(list(map(lambda x: x[1], data[i])))
                    result.update(list(map(lambda x: x[1], data[j])))
                    print("For pair", i, " and ", j, len(result))
                    maxL = max(maxL, len(result))
        return maxL

s=Solution()
#assert s.maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]) == 5
#assert s.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]) == 4
#assert s.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]) == 5
assert s.maximalNetworkRank(n=2, roads = [[1,0]]) == 1
assert s.maximalNetworkRank(n = 5, roads = [[2,3],[0,3],[0,4],[4,1]]) == 4
assert s.maximalNetworkRank(n=6, roads = [[2,4]]) == 1
