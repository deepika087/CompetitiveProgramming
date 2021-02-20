__author__ = 'deepika'

"""
Runtime: 76 ms, faster than 50.00% of Python online submissions for Minimum Length of String After Deleting Similar Ends.
Memory Usage: 14.5 MB, less than 100.00% of Python online submissions for Minimum Length of String After Deleting Similar Ends.

"""
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = len(s) - 1

        while left < right:
            leftChar = s[left]
            rightChar = s[right]

            if leftChar != rightChar:
                break

            while left < right and s[left] == rightChar:
                left += 1
            while right >= left and s[right] == leftChar:
                right -= 1


        return right - left + 1

s=Solution()
assert s.minimumLength("ca") == 2
assert s.minimumLength("cabaabac") ==0
assert s.minimumLength("aabccabba") == 3