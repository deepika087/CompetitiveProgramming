#!/bin/python

import sys


n = int(raw_input().strip())
squares = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)] # m is the number of squares and d is total sum which we need
# your code goes here

if (len(squares) < m):
    print "0"
else:
    result = 0
    firstM_sum = 0
    for i in range(0, m):
        firstM_sum = firstM_sum + squares[i]

    #print " initially sum = ", firstM_sum
    if (firstM_sum == d):
        result = result + 1
    for i in range(1,len(squares) - m + 1):

        firstM_sum = firstM_sum - squares[i-1]
        firstM_sum = firstM_sum + squares[m-1+i]
        #print " Will sum from i = ", i, " till last = ", i + m-1, " with sum = ", firstM_sum
        if (firstM_sum == d):
            result = result + 1
    print result



