class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        CharacterMapping=dict()
        for i in range(len(s)):
            if(s[i] == t[i]):
                if (CharacterMapping.get(s[i], -1) != -1 and t[i] != CharacterMapping.get(s[i])):
                    return False
                CharacterMapping[s[i]] = t[i]
                count = len(list(filter(lambda x: x == t[i], CharacterMapping.values())))
                if (count > 1):
                    return False
            else:
                if (CharacterMapping.get(s[i], -1) == -1):
                    CharacterMapping[s[i]] = t[i]
                    count = len(list(filter(lambda x: x == t[i], CharacterMapping.values())))
                    if (count > 1):
                        return False
                    #CharacterMapping[t[i]] = s[i]
                else:#Mapping already exists
                    #oldMapped = CharacterMapping.get(s[i])
                    if ( CharacterMapping.get(s[i]) != t[i]):
                        return False
                    else:
                        continue
        return True





if __name__=="__main__":
    s=Solution()
    print s.isIsomorphic("aba", "baa")
    print s.isIsomorphic("ab", "aa") #Expected Falses
    print s.isIsomorphic("ab", "ca") #Expected True
    print s.isIsomorphic("egg", "add")
    print s.isIsomorphic("foo", "bar")
    print s.isIsomorphic("paper", "title")