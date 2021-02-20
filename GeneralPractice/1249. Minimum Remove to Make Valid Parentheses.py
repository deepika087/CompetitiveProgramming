__author__ = 'deepika'

"""
Runtime: 644 ms, faster than 32.02% of Python online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 18.9 MB, less than 10.28% of Python online submissions for Minimum Remove to Make Valid Parentheses.

My idea was to related the starting opening bracket with nothing. But that wont worl example
()()(((
Now if I start from 0th element I end up disturbing the string instead

i = 0
while open > close:
    if duplicate[i] == '(':
        duplicate[i] = '*'
        open -= 1
    i = i + 1
"""

class Solution(object):
    def isOpen(self, character):
        return character == '('

    def isClose(self, character):
        return character == ')'

    def isBracket(self, character):
        return self.isopen(character) or self.isClose(character)

    def isChar(self, character):
        return not (character == ')' or character == '(')

    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        open = 0
        close = 0
        duplicate = []
        for i in range(len(s)):
            character = s[i]
            if self.isChar(character):
                duplicate.append(character)
                continue
            elif self.isOpen(character):
                duplicate.append(character)
                open = open + 1
            elif self.isClose(character):
                if open > close:
                    duplicate.append(character)
                    close += 1
                    continue
                else:
                    duplicate.append('*')

        open = 0
        close = 0
        for i in range(len(duplicate) - 1, -1, -1):
            if self.isClose(duplicate[i]):
                close += 1
            elif self.isOpen(duplicate[i]):
                if open >= close:
                    duplicate[i] = '*'
                else: #It means we found a matching open-close so decrease the close count.
                    close -= 1

        return ''.join(duplicate).replace('*', '')

s=Solution()
print(s.minRemoveToMakeValid("())()((("))
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("a)b(c)d"))
print(s.minRemoveToMakeValid("))(("))
print(s.minRemoveToMakeValid("(a(b(c)d)"))
print(s.minRemoveToMakeValid("(((ab(c))))"))





