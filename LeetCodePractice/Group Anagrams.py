"""
49. Group Anagrams

100 / 100 test cases passed.
Status: Accepted
Runtime: 289 ms
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams=dict()
        #print type(anagrams)
        for item in strs:
            temp=sorted(item)
            temp=''.join(temp)
            if (anagrams.get(temp, -1) == -1):
                anagrams[temp]=list()
            anagrams[temp].append(item)
        #print anagrams

        result=[]
        for (k,v) in anagrams.items():
            sorted(v)
            result.append(sorted(v))
            #anagrams[k] = sorted(v)
        result=sorted(result)
        return result
s=Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])