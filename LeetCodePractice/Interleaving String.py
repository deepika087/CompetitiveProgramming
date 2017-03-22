
"""
99 / 101 test cases passed.
Status: Time Limit Exceeded

Cann't handle really long inputs. For that use dp
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        print " s1 = ", s1, " s2 = ", s2, " and s3 = ", s3

        if(len(s1) == 0 and len(s2) == 0 and len(s3) == 0):
            return True
        elif ((s1 == "" and s2 == s3) or (s2 == "" and s1 == s3)):
            return True
        elif((len(s1) == 0 and len(s2) != 0 and len(s3) != 0) or (len(s1) == 0 and len(s2) != 0 and len(s3) != 0) or (len(s1) == 0 and len(s2) == 0 and len(s3) != 0)):
            return False
        if (len(s1) + len(s2) != len(s3)):
            return False
        if ( (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0]) and (len(s2) == 0 or (len(s2) > 0 and len(s3) >0 and  s2[0] != s3[0]))): #Match with s1 only
            return self.isInterleave(s1[1:], s2, s3[1:])
        elif ( ( len(s1) == 0 or len(s1) > 0 and len(s3) > 0 and s1[0] != s3[0]) and ( len(s2) > 0 and len(s3) >0 and s2[0] == s3[0])): #
            return self.isInterleave(s1, s2[1:], s3[1:])
        elif(len(s1) > 0 and len(s2) > 0 and len(s3) > 0 and s1[0] == s3[0] and s2[0] == s3[0]): #Both match
            return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:]) #Either incrmeent s1 or s2. s3 will be incremented in any case
        else:
            return False
s=Solution()
print s.isInterleave("","b", "b")
print s.isInterleave("aabcc","dbbca", "aadbbcbcac")
print s.isInterleave("aabcc","dbbca", "aadbbbaccc")