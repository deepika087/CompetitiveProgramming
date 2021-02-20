"""
219. Contains Duplicate II

20 / 20 test cases passed.
Status: Accepted
Runtime: 69 ms
Beats : 22%
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tracker=dict()
        for i in range(len(nums)):
            if (tracker.get(nums[i], -1) == -1):
                tracker[nums[i]] = i
            else: # Found duplicate
                old_i = tracker[nums[i]]
                if ( i - old_i <= k):
                    return True
                else:#Repeat but after k elements
                    tracker[nums[i]]=i
        return False