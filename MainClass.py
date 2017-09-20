__author__ = 'deepika'

import MainClassHelper as mcp


def mainFunction():
    val = mcp.say_hello()
    print val

subjects = {}
subjects['a'] = 3
subjects['b'] = 2
subjects['c'] = 1

def make_comparator():
    def compare(x, y):
        if x[1] < y[1]:
            return -1
        elif (x[1] > y[1]):
            return 1
        return 0
    return compare

print subjects
sortedDict = sorted(subjects.items(), cmp=make_comparator(), reverse=True)
print sortedDict