class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + "," +  str(self.end) + "]"

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if (len(intervals) in [1, 0]):
            return 0
        intervals = sorted(intervals, key=lambda i: (i.start, i.end))
        iend = intervals[0].end
        inoutIndex = 0
        i=1
        while( i < len(intervals)):
            if (intervals[i].start < iend):
                inoutIndex = inoutIndex + 1
            else:
                iend = intervals[i].end
            i = i + 1
        return inoutIndex


s=Solution()
print s.eraseOverlapIntervals(
    [
        Interval(1, 4),
        Interval(2, 5),
        Interval(10, 12),
        Interval(5, 9),
        Interval(5, 12)
    ]
)

print s.eraseOverlapIntervals(
    [
        Interval(1, 2),
        Interval(2, 3),
        Interval(1, 3),
        Interval(3, 4),
    ]
)

print s.eraseOverlapIntervals(
    [
        Interval(1, 2),
        Interval(1, 2),
        Interval(1, 2)
    ]
)
