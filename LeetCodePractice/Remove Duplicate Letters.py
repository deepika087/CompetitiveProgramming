
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        counter = 0;
        start = 0
        end = 0;
        for i in range(len(s)):
            if (counter & 1<<(i-'a') > 0): #Not the first occurence
                pass
            else:
                end = end + 1


s=Solution()
print s.removeDuplicateLetters("bcabc") #expected "abc"
print s.removeDuplicateLetters("cbacdcbc") #Expected "acdb"