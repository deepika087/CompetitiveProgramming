"""
67 / 67 test cases passed.
Status: Accepted
Runtime: 79 ms
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums=set()
        for item in nums:
            setNums.add(item)

        max_of_now = -1
        while setNums:
            count = 1
            target = setNums.pop()
            left, right = target - 1, target + 1
            while left in setNums:
                setNums.remove(left)
                count = count + 1
                left = left - 1
            while right in setNums:
                setNums.remove(right)
                count = count + 1
                right = right + 1
            max_of_now = max(max_of_now, count)
        return max_of_now



s=Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])