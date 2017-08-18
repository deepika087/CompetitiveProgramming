"""

154 / 154 test cases passed.
Status: Accepted
Runtime: 65 ms
Better than 94.4%
In this code I have used binary search to find potential indices and then  I have tried
to find leftPart, middlePart and rightPart using the indices received from binary search
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + "," +  str(self.end) + "]"

class Solution(object):

    def binary_search(self, intervals, x, left, right):
        if (left > right):
            return None
        mid = right - (right - left)/2
        if ( intervals[mid].start <= x <= intervals[mid].end):
            return mid
        if (x < intervals[mid].start):
            return self.binary_search(intervals, x, left, mid - 1)
        else:
            return self.binary_search(intervals, x, mid + 1, right)

    def find_interval_that_contains(self, intervals, x):
        return self.binary_search(intervals, x, 0, len(intervals) - 1)

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if (len(intervals) == 0):
            return [newInterval]

        start_index = self.find_interval_that_contains(intervals, newInterval.start)
        end_index = self.find_interval_that_contains(intervals, newInterval.end)
        if (start_index is not None and end_index is None):

            leftPart = intervals[0:start_index]
            midPart = [Interval(s=intervals[start_index].start, e=newInterval.end)]
            i = start_index
            while(i < len(intervals) and intervals[i].start < newInterval.end):
                i = i + 1
            i = len(intervals) - 1 if i > len(intervals) else i
            rightPart = intervals[i:]
            return leftPart + midPart + rightPart

        if (start_index is None and end_index is not None):
            i = 0
            while( i < len(intervals) and intervals[i].end < newInterval.start):
                i = i + 1
            leftPart = intervals[0:i]
            midPart = [Interval(s=newInterval.start, e=intervals[end_index].end)]
            rightPart = [] if end_index == len(intervals)-1 else intervals[end_index+1:]
            return leftPart + midPart + rightPart

        if (start_index is None and end_index is None):
            i = 0
            while(i < len(intervals) and intervals[i].start < newInterval.start):
                i = i + 1
            leftPart = intervals[0:i]
            while(i < len(intervals) and intervals[i].start < newInterval.end):
                i = i + 1

            midPart = [newInterval]
            rightPart = intervals[i:]
            return leftPart + midPart + rightPart

        intervals[start_index].end = intervals[end_index].end
        del intervals[start_index+1:end_index+1]
        return intervals

s=Solution()
print s.insert(
    [Interval(2,7),
     Interval(8, 8),
     Interval(10, 10),
     Interval(12, 13),
     Interval(16, 19)
    ],
    Interval(9, 17))
print s.insert([Interval(0,7), Interval(8, 8), Interval(9, 11)], Interval(4, 13))
print s.insert([Interval(0,5), Interval(9, 12)], Interval(7, 16))
print s.insert([Interval(1,5)], Interval(0, 6)) #[0, 6]
print s.insert([Interval(1,5)], Interval(6,8))  # [[1,5], [6,8]]
#start is None and end is None
print s.insert(
    [ Interval(1,3),
      Interval(6,9)
    ],
     Interval(4,5))

#start is None and end is not None
print s.insert(
    [ Interval(1,3),
      Interval(6,9)
    ],
     Interval(5,8))

#start is not None and end is None
print s.insert(
    [ Interval(1,3),
      Interval(6,9)
    ],
     Interval(2,5))

#start is not None and end is not None
print s.insert(
      [ Interval(1,2),
        Interval(3,5),
        Interval(6,7),
        Interval(8,10),
        Interval(12,16)
     ], Interval(4,9) )
