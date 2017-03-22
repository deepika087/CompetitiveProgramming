__author__ = 'deepika'

for w in sorted(d, key=d.get, reverse=True):
  print w, d[w]

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