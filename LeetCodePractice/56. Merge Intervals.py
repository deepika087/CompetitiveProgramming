# Definition for an interval.
"""
Accepted. performance is not that good  because I am popping and then inserting.
Rather than that result[-1] = max(of the two intervals in qs)

169 / 169 test cases passed.
Status: Accepted
Runtime: 95 ms

"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + "," +  str(self.end) + "]"

class Solution(object):
    def is_overlap(self, popped_interval, new_interval):
        return popped_interval.start <= new_interval.start <= popped_interval.end

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for interval in sorted(intervals, key=lambda i: i.start):
            if (len(result) == 0):
                result.append(interval)
            else:
                popped_interval = result.pop()
                if (self.is_overlap(popped_interval, interval)):
                    result.append(Interval(s=min(popped_interval.start, interval.start),
                        e=max(popped_interval.end, interval.end)))
                else:
                    result.append(popped_interval)
                    result.append(interval)
        return result

s=Solution()
print s.merge(
    [ Interval(1,3),
    Interval(2,6),
    Interval(8,10),
    Interval(15,18) ]
)
