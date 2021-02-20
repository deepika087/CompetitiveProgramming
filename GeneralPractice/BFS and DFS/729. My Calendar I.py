__author__ = 'deepika'


"""
The insert logic is completely screwed up. Basically binary search
Better way is the BST
"""
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

class MyCalendar(object):

    def __init__(self):
        self.intervals = []


    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        targetInterval = Interval(start, end)
        if len(self.intervals) == 0:
            self.intervals.append(targetInterval)
            return True

        idx = self.tryInsert(0, len(self.intervals)- 1, targetInterval)

        if idx == -1:
            return False
        if idx == -99:
            self.intervals.append(targetInterval)
        else:
            self.intervals.insert(idx, targetInterval)
        return True

    def disjoint(self, interval1 ,interval2):
        if interval2.start >= interval1.end:
            return True
        if interval2.end <= interval1.start:
            return True
        return False

    def after(self, interval1, interval2):
        if interval2.start >= interval1.end:
            return True
        return False

    def exactOverlap(self, interval1, interval2):

        if interval1.start == interval2.start and interval1.end == interval2.end:
            return True
        if interval2.start == interval1.end:
            return False
        if interval1.start <= interval2.start < interval1.end:
            return True
        if interval2.end == interval1.start:
            return False
        if interval2.start <= interval1.start < interval2.end:
            return True
        return False

    def tryInsert(self, lo, hi, targetInterval):
        if hi < lo:
            return lo
        if hi < 0 or lo < 0 :
            return 0
        if lo > len(self.intervals) or hi > len(self.intervals):
            return -99
        if lo == hi:
            if self.disjoint(self.intervals[lo], targetInterval):
                if self.after(self.intervals[lo], targetInterval):
                    return lo + 1
                else:
                    return lo
            return -1
        #print(" low = ", lo, " high = ", hi, " mid = ", hi - (hi - lo)/2)
        mid =   (lo+hi)/2 #hi - (hi - lo)/2

        if self.exactOverlap(self.intervals[mid], targetInterval):
            return -1

        if mid+1 < len(self.intervals) and self.after(self.intervals[mid], targetInterval) \
                and not self.after(self.intervals[mid+1], targetInterval):
            return mid+1

        if mid-1 >= 0 and not self.after(self.intervals[mid], targetInterval) \
            and self.after(self.intervals[mid-1], targetInterval):
            return mid-1

        if self.after(self.intervals[mid], targetInterval):
            return self.tryInsert(mid+1, hi, targetInterval)
        else:
            return self.tryInsert(lo, mid-1, targetInterval)


MyCalendar =MyCalendar()

input1 = ["MyCalendar","book","book","book","book","book","book","book","book","book","book"]
input2 = [[],[19,26],[3,10],[39,44],[35,40],[3,12],[5,13],[11,17],[47,50],[29,37],[26,34]]

true = True
false = False
#output = [true, true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
for i in range(1, len(input1)):
    if input1[i] == "book":
        if i == 9:
            print("start debugging")
        MyCalendar.book(input2[i][0], input2[i][1])
        print("done", i)

