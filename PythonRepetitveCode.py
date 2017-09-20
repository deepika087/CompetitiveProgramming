__author__ = 'deepika'



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

d=dict()
d[5] = 10
d[2] = 9
d[3] = 8
d[4] = 1
d[1] = -100

def make_comparator():
    def compare(x, y):
        print x, y
        return 1
    return compare

new_d = sorted(d.items(), key=lambda x: x[1])
print new_d[0][1], type(new_d)
for w in sorted(d, key=d.get, reverse=False):
    print w, d[w]
