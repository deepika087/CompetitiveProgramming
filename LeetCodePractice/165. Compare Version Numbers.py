

#If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version1 = map(lambda x: int(x), version1)

        version2 = version2.split(".")
        version2 = map(lambda x: int(x), version2)
        print version1, version2

        if (len(version1) <= len(version2)):
            return self.compareVersionUtil(version1, version2)
        else:
            result = self.compareVersionUtil(version2, version1)
            if result == 1:
                result = -1
            elif result == 1:
                result = 1
            else:
                result = 0
            return result

    def compareVersionUtil(self, version1, version2):
        if (len(version1) == 0):
            if (len(version2) == 1 and version2[0] == 0):
                return 0
            else:


s=Solution()
print s.compareVersion("13.1.1", "13.1.1.00")
