__author__ = 'deepika'
"""
35 / 35 test cases passed.
Status: Accepted
Runtime: 129 ms
"""
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictionary = {}
        for _ in s:
            if (dictionary.get(_, None) == None):
                dictionary[_] = 1
            else:
                dictionary[_] = dictionary[_] + 1


        sortedDict = sorted(dictionary.items(), key=(lambda x: x[1]), reverse=True)
        result = [k*v for (k, v) in sortedDict]
        return "".join(result)


s=Solution()
print s.frequencySort("tree")
print s.frequencySort("cccaaa")
print s.frequencySort("Aabb")
