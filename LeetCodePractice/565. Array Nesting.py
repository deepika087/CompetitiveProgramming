__author__ = 'deepika'

"""

856 / 856 test cases passed.
Status: Accepted
Runtime: 92 ms
"""
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -1
        visited = [None for i in range(len(nums))]
        for i in range(len(nums)):
            if visited[i]:
                continue
            max_so_far = max(max_so_far, self.dfs(nums, i, visited))
        return max_so_far

    def dfs(self, nums, start, visited):
        i = start
        count = 0
        while count == 0 or i != start:
            visited[i] = True
            i = nums[i]
            count = count + 1
        return count

s=Solution()
print s.arrayNesting([5,4,0,3,1,6,2])