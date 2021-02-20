__author__ = 'deepika'

#Now it is fine. It wasn't decreasing number of rooms every time end time was encountered.
# answer should be 3.
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
        maxCount = 0
        while(i < len(startArray) and j < len(endArray)):
            print(i, j)
            if (startArray[i] < endArray[j]):
                meetingRooms = meetingRooms + 1
                maxCount = max(maxCount, meetingRooms)

            else:
                meetingRooms -= 1
                j = j + 1
            i = i + 1
        return maxCount

s=Solution()

print s.minMeetingRooms(
    [
        Interval(1, 17),
        Interval(7, 20),
        Interval(10, 30),
        Interval(31, 35),
        Interval(33, 36)
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
print s.minMeetingRooms(
    [
        Interval(10,16),
        Interval(2,8),
        Interval(1,6),
        Interval(7,12)

    ]
)
print s.minMeetingRooms(
    [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20),
        Interval(6, 16)
    ]
)