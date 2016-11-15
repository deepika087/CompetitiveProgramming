"""
217. Contains Duplicate
17 / 17 test cases passed.
Status: Accepted
Runtime: 69 ms
"""
class Solution(object):
    """
    Cannot handle negative numbers
    """
    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter=0
        for item in nums:
            if ( counter & 1<<item > 0):
                return True
            counter = counter | 1<<item
        return False

    def containsDuplicate(self, nums):
        tracker=dict()
        for item in nums:
            if (tracker.get(item, -1) == -1):
                tracker[item] = 1
            else:
                return True
        return False

s=Solution()
print s.containsDuplicate([1, 2, 3 ])
print s.containsDuplicate([1, 2, 3, 3])