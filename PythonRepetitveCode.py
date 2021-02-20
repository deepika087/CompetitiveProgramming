




"""
def make_comparator(less_than):
    def compare(x, y):
        if less_than(x, y):
            return -1
        elif less_than(y, x):
            return 1
        else:
            return 0
    return compare

sortedDict = sorted(subjects, cmp=make_comparator(cmpValue), reverse=True)
"""


"""
Threading
def newF():
    for x in range(n):
        whatever code.

t1 = Thread(target=newF)
t1.start()
t1.join()
"""

d=dict()
d[5] = 10
d[2] = 9
d[3] = 8
d[4] = 1
d[1] = -100

def make_comparator():
    def compare(x, y):
        if x[1] < y[1]:
            return 1
        elif x[1] > y[1]:
            return -1
        else:
            return 0
    return compare

print("Using comparator")
d1=sorted(d.items(), cmp=make_comparator())
print(d1)
new_d = sorted(d.items(), key=lambda x: x[1])
print new_d[0][1], type(new_d)
for w in sorted(d, key=d.get, reverse=False):
    print w, d[w]


class Solution:

    def customComparator(self, x, y):
        if x.start < y.start :
            return -1
        if x.start > y.start:
            return 1

        if x.end < y.end:
            return 1
        elif x.end > y.end:
            return -1
        return 0

    def findOverlap(self, intervals):

        intervals = sorted(intervals, cmp=self.customComparator)
        print(intervals)
