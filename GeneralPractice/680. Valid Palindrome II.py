__author__ = 'deepika'

class Solution(object):
    def isPal(self, s, left, right):

        while (left < len(s) and right >= 0 and s[left] == s[right]):
            left += 1
            right -= 1
        return left >= right

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        deleteChar = 0
        while (left < len(s) and right >= 0 and left <= right):
            if (s[left] == s[right]):
                left += 1
                right -= 1
            else:
                if (self.isPal(s, left, right - 1)):
                    return True
                if (self.isPal(s, left + 1, right)):
                    return True
                return False
        return True




s=Solution()

print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
