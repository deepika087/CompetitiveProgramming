__author__ = 'deepika'


class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """


        dict = {}

        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 0
            dict[s[i]] += 1

        values = dict.values()
        values = sorted(values)

        left = 0
        right = left + 1

        min_deletions = 0
        while right < len(values) and len(set(values)) != len(values):

            while right < len(values):
                if values[left] == values[right]:
                    if left == 0:
                        values[left] -= 1
                        min_deletions = 1
                    else:
                        oldValue = values[left]
                        if values[left] == values[left - 1] + 1:
                            values[left] = values[left - 1] - 1
                        else:
                            values[left] -= 1
                        if values[left] < 0:
                            values[left] = 0
                        min_deletions += oldValue - values[left]

                left += 1
                right = left + 1

        return min_deletions

s=Solution()

assert s.minDeletions("accdcdadddbaadbc") == 1
assert s.minDeletions("abcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwzabcdefghijklmnopqrstuvwxwz") == 276
assert s.minDeletions("bbcebab") == 2
assert s.minDeletions("abcabc") == 3
print("!!!!!!!!!!!!!!!!!!!")
assert s.minDeletions("aab") == 0
assert s.minDeletions("aaabbbcc") == 2
assert s.minDeletions("ceabaacb") == 2

