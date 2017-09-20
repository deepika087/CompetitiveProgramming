__author__ = 'deepika'

"""
104 / 104 test cases passed.
Status: Accepted
Runtime: 212 ms
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        queue = list()
        seenSet = set()

        for i in range(len(s)):
            _char = s[i]
            if _char not in seenSet:
                queue.append(_char)
                seenSet.add(_char)
            elif _char in seenSet:
                if _char in queue:
                    queue.remove(_char)
                else:
                    continue
        if len(queue) == 0:
            return -1
        popped = queue.pop(0)
        return s.find(popped)

s=Solution()
print s.firstUniqChar("leetcode")
print s.firstUniqChar("loveleetcode")
