__author__ = 'deepika'
"""
200 / 200 test cases passed.
Status: Accepted
Runtime: 39 ms

Better than 85.58%
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (len(prices) in [0, 1]):
            return 0
        min_ele = prices[0]
        profit = 0
        for i in range(len(prices)):
            if (prices[i] > min_ele):
                profit = max(profit, prices[i] - min_ele)
            if (prices[i] < min_ele):
                min_ele = prices[i]
        return profit


s=Solution()
assert(s.maxProfit([7, 1, 5, 3, 6, 4]) == 5)
assert(s.maxProfit([7, 6, 4, 3, 1]) == 0)