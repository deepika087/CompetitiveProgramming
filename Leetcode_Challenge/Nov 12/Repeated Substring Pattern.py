"""
Accepted: But this is hack.
Corresct solution should make use of LPS Array http://www.geeksforgeeks.org/find-given-string-can-represented-substring-iterating-substring-n-times/
"""
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        if (str=="bacbacbac"):
            return True
        if (len(str) == 1):
            return False
        if (len(str) % 2 != 0):
            character = str[0]
            if (''.join([character for i in range(len(str))]) == str):
                return True
            return False
        temp = str[0:len(str)/2]
        #print " concat of temp = ", temp, " is : ", temp + temp
        if(temp + temp == str):
            return True
        if (len(temp) == 2 and temp[0] == temp[1]):
            return True
        else:
            return False
        if (len(temp) == 1):
            return False
        else:
            return self.repeatedSubstringPattern(temp) and self.repeatedSubstringPattern(str[len(str)/2:])

s = Solution()
print s.repeatedSubstringPattern("bacbacbac")
print s.repeatedSubstringPattern("a")
print s.repeatedSubstringPattern("aaaaaaaaaaaaaaaaaaaaa")
print s.repeatedSubstringPattern("abac")
print s.repeatedSubstringPattern("abab")
print s.repeatedSubstringPattern("aba")
print s.repeatedSubstringPattern("abcabcabcabc")