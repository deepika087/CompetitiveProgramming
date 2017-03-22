__author__ = 'deepika'

#!/bin/python

import sys

def isclosebracket(bracket):
    if (bracket == ')' or bracket == ']' or bracket == '}'):
        return True
    return False

def isopeningbracket(bracket):
    if ((bracket == '(' or bracket == '[' or bracket == '{')):
        return True
    return False

def isTopMatching(arr, bracket):
    if (len(arr) == 0):
        return False
    ele = arr.pop(-1)
    #print " Element popped: ", ele
    if (ele == '(' and bracket == ')'):
        return True
    if (ele == '[' and bracket == ']'):
        return True
    if(ele == '{' and bracket == '}'):
        return True

    return False

def checkifbalanced(s):
    if (s is None):
        return True
    arr = list()

    if (isclosebracket(s[0]) and len(arr) ==0 ):
        return False

    for i in range(0, len(s)):
        if (isopeningbracket(s[i])):
            arr.append(s[i])
            #print "Arr", arr, " at i = ", i
        elif (isclosebracket(s[i]) and isTopMatching(arr, s[i])):
            continue
        else:
            return False

    if (len(arr) == 0):
        return True
    return False

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    print "YES" if checkifbalanced(s) else "NO"