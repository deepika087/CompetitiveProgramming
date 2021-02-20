__author__ = 'deepika'

"""
this approach will not work. You have to use binary search to find the next greater index.
Google question

"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __hash__(self):
        return self.start.__hash__() + self.end.__hash__()

    def __str__(self):
        return "(" + str(self.start) + " , " + str(self.end) + ")"

    def __repr__(self):
        return self.__str__()


class Solution(object):
    def overlap(self, top, incoming):
        return incoming.end < top.end or top.start < incoming.start < top.end

    def greater(self, top, incoming):
        return incoming.start >= top.end

    def findRightInterval(self, intervals):
        intervals = [ Interval(x[0], x[1]) for x in intervals]
        #print(type(intervals))
        #print(type(intervals[0]))
        if (len(intervals) == 1):
            return  [-1]

        intervalDict = dict()
        for i in range(len(intervals)):
            intervalDict[intervals[i]] = i

        intervals = sorted(intervals, key=lambda x: x.start)
        print("sorted")
        print(intervals)
        stack = []
        result = [-1 for _ in range(len(intervals))]

        #print(intervalDict)
        i = 0
        while i < len(intervals):
            print("processing incoming : " + str( intervals[i]))
            incoming = intervals[i]

            if len(stack) == 0:
                stack.append(incoming)
                i = i + 1
                continue

            top = stack[-1]


            print("stack is : ", str(stack))
            if self.overlap(top, incoming):
                stack.append(incoming)


            elif self.greater(top, incoming):
                while len(stack) > 0 and self.greater(top, incoming):
                    top = stack.pop()
                    result[intervalDict[top]] = intervalDict[incoming]
                    top = stack[-1] if len(stack) > 0 else None
                stack.append(incoming)
            else:
                pass
            i = i + 1
        return result
s=Solution()
#print(s.findRightInterval([ [1, 4], [2, 3], [3, 4] ] ))
#print(s.findRightInterval([ [1,2] ]))
#print(s.findRightInterval([ [3, 4], [2, 3], [1, 4] ] ))

#print(s.findRightInterval([ [3, 4], [4, 5], [2, 3], [1, 4] ] ))
#print(s.findRightInterval([ [1, 4], (4, 5), (2, 3), [3, 4] ] ))

print(s.findRightInterval( [[-100,-98],[-99,-97],[-98,-96] ]))
#print(s.findRightInterval([ [1, 4], (4, 5), (2, 3), [3, 4] ] ))
