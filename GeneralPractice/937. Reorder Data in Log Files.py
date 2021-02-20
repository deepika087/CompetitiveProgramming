__author__ = 'deepika'


class Solution(object):
    def isdigit(self, char):
        if 0 <= ord(char) - ord('0') <= 9:
            return True
        return False

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digitLog = []
        charLogs = []
        for log in logs:
            idx = log.find(' ');
            if (self.isdigit(log[idx + 1])):
                digitLog.append(log)
            else:
                charLogs.append(log)

        charLogs = sorted(charLogs)
        charLogs.extend(digitLog)
        return charLogs

s=Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
