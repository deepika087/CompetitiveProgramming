
# Definition for an interval.
import operator
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[ " + str(self.start) + ", " + str(self.end) + "]"

class Solution(object):
    def isCompatible(self,point1, point2):
        if (point1.start == point2.start and point1.end == point2.end):
            return False
        return (point1.start < point2.start and point1.end <= point2.start) \
               #or (point2.start < point1.start and point2.end <= point1.start)

    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=operator.attrgetter('start', 'end'))
        res = lo = 0
        print intervals
        for hi in range(1, len(intervals)):
            if intervals[lo].end > intervals[hi].start:
                res += 1
            if not intervals[hi].start < intervals[lo].end < intervals[hi].end:
                lo = hi
                print " New lo = ", intervals[lo]
        return res

    """
    This DP doesn;t work + this is not a dp problem
    """
    def eraseOverlapIntervals1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        N = len(intervals)
        if (N==0):
            return 0
        if (N==1):
            return 0
        #sort Intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        print "After soring ", intervals

        latest=[ [ Interval() for i in range(N) ] for j in range(N)]
        data = [ [0 for i in range(N)] for j in range(N) ]
        for i in range(N):
            data[i][i] = 1
            latest[i][i] = intervals[i]

        #print latest
        for l in range(2, N+1):
            for i in range(N-1, -1, -1):
                j = i + l - 1
                if (j < N):
                    if ( l == 2 and (self.isCompatible(intervals[j-1], intervals[j]) or self.isCompatible(intervals[j], intervals[j-1]))):
                        data[i][j] = 2
                        latest[i][j] = intervals[j] if intervals[j-1].end <= intervals[j].start else intervals[j-1]
                        #print " i = ", i, " j = ", j, " to ", latest[i][j]
                    else:
                        if ( self.isCompatible(latest[i][j-1], latest[i+1][j]) or self.isCompatible(latest[i+1][j], latest[i][j-1])):
                            data[i][j] = max(data[i][j-1], data[i+1][j]) + 1
                            latest[i][j] = latest[i+1][j] if latest[i][j-1].end <= latest[i+1][j].start else latest[i][j-1]
                        else:
                            if (data[i][j-1] > data[i+1][j]):
                                data[i][j] = data[i][j-1]
                                latest[i][j] = latest[i][j-1]
                            else:
                                data[i][j] =  data[i][j-1]
                                latest[i][j] = latest[i][j-1]
                                """
                                if (latest[i+1][j].end > latest[i][j-1].end):
                                    data[i][j] =  data[i+1][j]
                                    latest[i][j] = latest[i+1][j]
                                else:
                                    data[i][j] =  data[i][j-1]
                                    latest[i][j] = latest[i][j-1]
                                """

        print data
        print latest
        return 0 if data[0][N-1] == N else N - data[0][N-1]


if __name__ =="__main__":
    s=Solution()
    intervals = []
    intervals.append(Interval(1,2))
    intervals.append(Interval(2,3))
    intervals.append(Interval(3,4))
    intervals.append(Interval(1,3))
    print s.eraseOverlapIntervals(intervals)

    intervals=[]
    intervals.append(Interval(1,2))
    intervals.append(Interval(1,2))
    intervals.append(Interval(1,2))
    print s.eraseOverlapIntervals(intervals)

    intervals=[]
    intervals.append(Interval(1,2))
    intervals.append(Interval(2,3))
    print s.eraseOverlapIntervals(intervals)

    #[[1,100],[11,22],[1,11],[2,12]]
    intervals=[]
    intervals.append(Interval(1,100))
    intervals.append(Interval(11,22))
    intervals.append(Interval(1,11))
    intervals.append(Interval(2,12))
    print s.eraseOverlapIntervals(intervals)

    #[[0,1],[3,4],[1,2]]
    intervals=[]
    intervals.append(Interval(0,1))
    intervals.append(Interval(3,4))
    intervals.append(Interval(1,2))
    print s.eraseOverlapIntervals(intervals)

"""
for i in range(N):
            for l in range(2, N+1):
                j = i + l - 1
                if (j < N):
                    print " Comparing ", intervals[j], " and ", intervals[j-1]
                    if(self.isCompatible(intervals[j-1], intervals[j])):
                        data[i][j]=data[i][j-1] + 1
                    else:
                        data[i][j]=data[i][j-1]
"""