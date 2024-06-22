import copy
import sys

"""

Incorrect solution.

"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pCounter = [ -1 for i in range(60)]
        for i in range(0, len(t)):
            if (pCounter[ord(t[i]) - ord('A')] == -1):
                pCounter[ord(t[i]) - ord('A')] = pCounter[ord(t[i]) - ord('A')] + 2
            else:
                pCounter[ord(t[i]) - ord('A')] = pCounter[ord(t[i]) - ord('A')] + 1
        i = 0
        min_length_so_far = sys.maxint
        min_start = -1
        while(i < len(s)):
            if (pCounter[ord(s[i]) - ord('A')] == -1):
                i = i + 1
            else:
                start = i
                pTemp = copy.copy(pCounter)
                pTemp[ord(s[i]) - ord('A')] = pTemp[ord(s[i]) - ord('A')] - 1
                i=i+1
                pSizeTemp = 1
                if (len(t) == 1):
                    min_length_so_far = 1
                    min_start = start

                while(True):
                    if (i >= len(s) ):
                        break;
                    if (pTemp[ord(s[i]) - ord('A')] == -1):
                        pass
                    elif (pTemp[ord(s[i]) - ord('A')] > 0):
                        pTemp[ord(s[i]) - ord('A')] = pTemp[ord(s[i]) - ord('A')] - 1 #till not hit some 'i' whose occrences have been seen alrady
                        #i = i + 1
                        pSizeTemp = pSizeTemp  + 1
                    else:#All occurences of this character has been seen
                        break;
                    if (pSizeTemp == len(t)):
                        if (i - start  < min_length_so_far):
                            #print " At i= ", i
                            min_length_so_far = i - start
                            min_start = start
                            print " Probable start is ", min_start, " of min length ", min_length_so_far
                            #i = start + 1
                            break;
                    i = i + 1

                #Either I have seen the entire window T and know next probab; window starts or
        if (min_start == -1):
            return ""
        else:
            return s[min_start:min_start + min_length_so_far ]

s=Solution()
print s.minWindow("cabeca", "cae")
print s.minWindow("a", "a")
print s.minWindow("ADOBECODEBANC", "ABC")