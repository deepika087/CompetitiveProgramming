__author__ = 'deepika'


"""
Runtime: 764 ms, faster than 58.05% of Python online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
Memory Usage: 45.2 MB, less than 5.85% of Python online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
"""

class Solution(object):
    def _getTime(self, t1):

        total = 0
        parts = t1.split(':')

        total += int(parts[0]) * 60
        total += int(parts[1])

        return total

    def checkWithinHour(self, t1, t2 ):

        t1 = self._getTime(t1)
        t2 = self._getTime(t2)
        #print(t1, t2, t2 - t1 <= 60)

        return t2 - t1 <= 60

    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """


        self.dict = {}
        result = set()
        for i in range(len(keyName)):
            if keyName[i] not in self.dict:
                self.dict[keyName[i]] = []
            self.dict[keyName[i]].append(keyTime[i])
        #print(self.dict)

        for (k, v) in self.dict.items():
            #print("Iterating for k : ", k)
            v.sort()

            for i in range(len(v) - 2):
                if self.checkWithinHour(v[i], v[i + 2]):
                    result.add(k)
                    break

        return list(sorted( result))

s=Solution()
print(s.alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
print(s.alertNames(keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]))
print(s.alertNames(keyName = ["a","a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","d","d","d","d","d","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h"],
keyTime = ["03:42","13:31","20:11","19:10","02:28","23:07","18:03","19:46","01:11","10:05","02:23","04:48","17:22","16:28","04:55","16:18","21:08","06:03","18:25","20:03","03:12","22:51","06:35","14:06","06:48","21:45","00:12","02:21","13:03","06:34","10:20","11:40","00:56","05:17","08:26","23:42","03:22","12:44","09:00","00:57","07:04","08:44","06:10","19:16","06:59","14:24","08:05","18:06","15:10","14:31","17:28","06:24","11:33","07:41","15:43","22:57","22:02","12:42","19:19","06:50","15:02","16:14","13:30","13:34","22:19"]))