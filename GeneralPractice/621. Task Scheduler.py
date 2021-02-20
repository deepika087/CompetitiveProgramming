__author__ = 'deepika'


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        hashMap = [ 0 for i in range(26)]
        for t in tasks:
            hashMap[ord(t) - ord('A')] = hashMap[ord(t) - ord('A')] + 1

        hashMap.sort()

        max_value = max(hashMap) - 1

        slots = max_value * n

        i = 24
        while i >= 0:
            _inp = hashMap[i]
            slots = slots - min(_inp, max_value)
            i = i - 1
        if slots > 0:
            return slots + len(tasks)

        return len(tasks)
s=Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))