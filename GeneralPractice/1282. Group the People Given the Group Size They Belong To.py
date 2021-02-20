__author__ = 'deepika'


"""
Runtime: 52 ms, faster than 99.76% of Python online submissions for Group the People Given the Group Size They Belong To.
Memory Usage: 12.6 MB, less than 99.06% of Python online submissions for Group the People Given the Group Size They Belong To.

Important thing is to form groups.
"""
class Solution(object):

    def _form_groups(self, array, size):
        results = []

        i = 0
        while i < len(array):
            results.append( array[i : i + size])
            i += size

        return results

    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        dictionary = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] not in dictionary:
                dictionary[groupSizes[i]] = []
            dictionary[groupSizes[i]].append(i)

        results = []
        for k,v in sorted(dictionary.items()):
            if len(v) <= k:
                results.append(v)
            else:
                results.extend(self._form_groups(v, k))

        return  results

s=Solution()
print(s.groupThePeople([3,3,3,3,3,1,3])) # [[5],[0,1,2],[3,4,6]]
print(s.groupThePeople([2,1,3,3,3,2])) #[[1], [0, 5], [2, 3, 4]]

