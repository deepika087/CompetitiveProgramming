__author__ = 'deepika'


class Solution:

    def equalCharAndNumber(self, string):

        sum_so_far = 0
        indices = dict()
        indices[0] = -1

        candidate = -float('inf')

        for i in range(len(string)):
            if 'a' <= string[i] <'z':
                sum_so_far += 1
            else:
                sum_so_far -= 1
            if sum_so_far not in indices: # I have never seen it just add to indices and move on
                indices[sum_so_far] = i
            else:
                candidate = max(candidate, i - indices[sum_so_far])
        return candidate

s=Solution()
print(s.equalCharAndNumber("abcde123"))
print(s.equalCharAndNumber("a1"))
print(s.equalCharAndNumber("a1b2"))
print(s.equalCharAndNumber("abcde123lmnop123345"))