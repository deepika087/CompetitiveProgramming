__author__ = 'deepika'

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + "," +  str(self.end) + "]"

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if (len(intervals) == 0):
            return 0
        if (len(intervals) == 1):
            return 1
        startArray = list(map(lambda x: x.start, intervals))
        endArray = list(map(lambda x: x.end, intervals))
        startArray.sort()
        endArray.sort()

        meetingRooms = 0
        i=0
        j=0
        while(i < len(startArray) and j < len(endArray)):
            if (startArray[i] < endArray[j]):
                meetingRooms = meetingRooms + 1

            else:
                j = j + 1
            i = i + 1
        return meetingRooms

s=Solution()

print s.minMeetingRooms(
    [
        Interval(1, 17),
        Interval(7, 10),
        Interval(12, 14)
    ]
)
print s.minMeetingRooms(
    [
        Interval(7, 10),
        Interval(2, 4)
    ]
)
print s.minMeetingRooms(
    [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]
)
[[7,10],[2,4]]
