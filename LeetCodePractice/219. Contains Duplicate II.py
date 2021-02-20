__author__ = 'deepika'


class Solution(object):
    #not working
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dictionary = dict()
        for i in range(len(nums)):
            if nums[i] in dictionary:
                nums[i].append(i)
                if any(lambda x: x >= abs(i - k) and x <= i + k, nums ):
                    #i + k in nums[i] or abs(i - k) in nums[i]: #Here is the error.
                    #Any value from i + k to i -k should be checked not only binary
                    return True
            else:
                dictionary[nums[i]] = [i]
        return False

    #Working
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