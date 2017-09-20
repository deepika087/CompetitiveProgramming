__author__ = 'deepika'

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        citations = sorted(citations, reverse=True)
        #print citations
        result = []
        for i in range(len(citations)):
            if citations[i] == i+1:
                result.append(citations[i])

        return max(result)

s=Solution()
print s.hIndex([3, 0, 6, 1, 5])