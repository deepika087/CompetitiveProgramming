__author__ = 'deepika'

"""
460 / 460 test cases passed.
Status: Accepted
Runtime: 292 ms

Better than 24.49%
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
          return False

        if len(s) == 1:
          return False

        left = 0
        right = len(s) - 1
        deleteChar = False
        while left < right:
            if s[left] == s[right]:
              left = left + 1
              right = right - 1
              continue
            else:
              return self.isPalin(s, left + 1, right) or self.isPalin(s, left, right - 1)
        return True


    def isPalin(self, s, left, right):
      while left < right:
        if s[left] == s[right]:
          left = left + 1
          right = right - 1
          continue
        else:
          return False
      return True


s = Solution()
print s.validPalindrome("aba")
print s.validPalindrome("abca")

