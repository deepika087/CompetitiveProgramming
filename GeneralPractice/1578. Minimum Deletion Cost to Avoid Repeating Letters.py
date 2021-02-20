__author__ = 'deepika'


"""
Incomplete but I got the Algo
"""
import sys
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """

        if len(s) in [0, 1]:
            return 0

        overall_result = 0
        window_max_cost = -1
        window_sum = 0
        i = 0
        for i in range(0, len(s)):
            if i > 0 and s[i] == s[i-1]:
                window_sum += cost[i]
                window_max_cost = max(cost[i], window_max_cost)
            else:
                overall_result += 0 if window_sum == -1 else window_sum - window_max_cost
                window_max_cost = -1 # rest the value
                window_sum = 0
        overall_result += 0 if window_sum == -1 else window_sum - window_max_cost
        print(overall_result)
        return overall_result

s=Solution()
assert s.minCost(s = "abaac", cost = [1,2,3,4,5]) == 3
assert s.minCost(s = "abc", cost = [1,2,3]) == 0
assert s.minCost(s = "aabaa", cost = [1,2,3,4,1]) == 2
