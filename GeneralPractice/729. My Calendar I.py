__author__ = 'deepika'

"""
Almost correct. Somewhere I have missed a boundary condition
"""
class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]"

class œMyCalendar(object):

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
        if interval2.end < interval1.start:
            return True
        return False

    def after(self, interval1, interval2):
        if interval2.start >= interval1.end:
            return True

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
        if hi < 0 or lo < 0 :
            return 0
        if lo > len(self.intervals) or hi > len(self.intervals):
            return -99
        if lo == hi:
            if self.disjoint(self.intervals[lo], targetInterval):
                if self.after(self.intervals[lo], targetInterval):
                    return lo + 1
                else:
                    return lo - 1 if lo > 0 else 0
            return -1
        #print(" low = ", lo, " high = ", hi, " mid = ", hi - (hi - lo)/2)
        mid =   (lo+hi)/2 #hi - (hi - lo)/2

        if self.exactOverlap(self.intervals[mid], targetInterval):
            return -1

        if self.after(self.intervals[mid], targetInterval):
            return self.tryInsert(mid+1, hi, targetInterval)
        else:
            return self.tryInsert(lo, mid-1, targetInterval)



"""
obj = MyCalendar()
assert obj.book(1, 5) == True
assert obj.book(5, 10) == True
assert obj.book(10, 20) == True
assert obj.book(10, 20) == False
assert obj.book(99, 100) == True

obj2 = MyCalendar()
assert obj2.book(1, 5) == True
assert obj2.book(5, 10) == True
assert obj2.book(10, 20) == True
assert obj2.book(20, 30) == True
assert obj2.book(99, 100) == True


obj3 = MyCalendar()
assert obj3.book(1, 5) == True
assert obj3.book(1, 2) == False
assert obj3.book(1, 3) == False
assert obj3.book(4, 5) == False
assert obj3.book(99, 100) == True

"""


obj4 = MyCalendar()
assert obj4.book(47,50) == True
assert obj4.book(33,41) == True
assert obj4.book(39,45) == False
assert obj4.book(33,42) == False
assert obj4.book(25,32) == True
assert obj4.book(26,35) == False
assert obj4.book(19,25) == True
assert obj4.book(3,8) == True
assert obj4.book(8, 13) == True
assert obj4.book(18, 27) == False


obj5 = MyCalendar()
assert obj5.book(1,7) == True
assert obj5.book(14,20) == True
assert obj5.book(20,29) == True
assert obj5.book(36,42) == True
assert obj5.book(44,50) == True
assert obj5.book(21,29) == True
assert obj5.book(34,40) == False