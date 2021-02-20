__author__ = 'deepika'

#candy crush problem.

class Solution:

    def collapse(self, string):

        if len(string) in [0, 1, 2]:
            return string

        stack = []

        i = 0
        while i < len(string):
            if len(stack) == 0 or stack[-1][0] != string[i]: #i == len(string) - 1
                stack.append( (string[i], 1) )
                i += 1
                continue

            if len(stack) > 0 and stack[-1][0] == string[i] and stack[-1][1] == 1:
                stack.append( (string[i], 2))
                i += 1
                continue


            if len(stack) > 0 and stack[-1][0] == string[i] and stack[-1][1] == 2:
                save = string[i]
                #Take care of characters ahead consider cc(c)ccc. At third c, you not only want to pop twice but also want to handle the
                # 'c' ahead
                while i < len(string) and string[i] == stack[-1][0]:
                    i += 1
                while len(stack) > 0 and stack[-1][0] == save: #Take care of the characters in stack
                    stack.pop()
                continue

        print(stack)

        return '' if len(stack) == 0 else ''.join(map(lambda x: x[0], stack))

s=Solution()
assert s.collapse("abccccbba") == "aa"
assert s.collapse("aabbccddeeedcba") == ''
assert s.collapse("aaaaaa") == ''
assert s.collapse("aaaaaabbbbbb") == ''
assert s.collapse("ababaababa") == "ababaababa"
assert s.collapse("abccc") == "ab"
assert s.collapse("abcd") == "abcd"
print("completed test cases")
