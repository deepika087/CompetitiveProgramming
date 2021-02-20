__author__ = 'deepika'
import sys
#output = [sys.maxint]*len("ABCSD")
#print output
"""
Given a string
"""


def function(string, key):
    arr = [0 for i in range(len(string))]
    leftIndex = sys.maxint
    for i in range(len(string)):
        if string[i] == key:
            leftIndex = i
            arr[i] = 0
        else:
            arr[i] = abs(i - leftIndex)


    rightIndex = sys.maxint
    for i in range(len(string)-1, -1, -1):
        if string[i] == key:
            rightIndex = i
        else:
            arr[i] = min(arr[i], abs(i - rightIndex))

    print arr

function("BLOOMBERG", "B")

length = []
print length