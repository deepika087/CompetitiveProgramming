

#If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0
        while i< len(version1) and version1[i] == '0':
            i = i + 1
        version1 = version1[i:]

        i = 0
        while i < len(version2) and version2[i] == '0':
            i = i + 1
        version2 = version2[i:]

        version1 = version1.split(".")
        version1 = None if len(version1) == 0 else [int(x) for x in version1]

        version2 = version2.split(".")
        print "len(version2)", len(version2)
        version2 = None if len(version2) == 0 else [int(x) for x in version2]
        print version1, version2

        if version1 == None and version2 is not None:
            return -1
        elif version1 is not None and version2 == None:
            return 1
        elif version1 is  None and version2 is None:
            return 0

        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            part1 = -1 if i >= len(version1) else version1[i]
            part2 = -1 if j >= len(version2) else version2[j]

            if part1 == part2:
                i = i + 1
                j = j + 1
                if i == len(version1) and j == len(version2):
                    return 0
            elif part1 < part2:
                return -1
            else:
                return 1


s=Solution()
#print s.compareVersion("13.1.1", "13.1.1.00")
#print s.compareVersion("01", "1")
print s.compareVersion("1", "0")

