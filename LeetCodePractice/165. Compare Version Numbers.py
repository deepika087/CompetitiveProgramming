__author__ = 'deepika'
"""
71 / 71 test cases passed.
Status: Accepted
Runtime: 42 ms
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #print version1
        version1 = version1.split(".")
        version1 = map(lambda x: int(x), version1)

        version2 = version2.split(".")
        version2 = map(lambda x: int(x), version2)

        #print version1, version2
        if (len(version1) <= version2):
            return self.compareVersionUtil(version1, version2)
        else:
            result = self.compareVersionUtil(version2, version1)
            if (result == -1):
                return 1
            if (result == 1):
                return -1
            return 0

    def compareVersionUtil(self, version1, version2):
        element1 = 0 if len(version1) == 0 else version1[0]
        element2 = 0 if len(version2) == 0 else version2[0]

        if (element1 < element2):
            return -1
        elif (element1 > element2):
            return 1
        elif (len(version1) <= 1 and len(version2) <= 1): #This was the last elemt
            return 0
        else:
            return self.compareVersionUtil(version1[1:], version2[1:])

s=Solution()
print s.compareVersion("1.3.0", "1.3.0.0")
print s.compareVersion("1.0.0", "1.0.0.0.1")



