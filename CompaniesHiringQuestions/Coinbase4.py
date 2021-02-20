__author__ = 'deepika'

"""
def numberOfRoutes (a):
    m = len(a)
    n = len(a[0])
    count = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):

        count[i][0] = a[i][j]

    for j in range(n):
        count[0][j] = a[0][j]

    for i in range(1, m):
        for j in range(1, n):
            if a[i][j] == 0:
               count[i][j] = 0
            else:
               count[i][j] = count[i-1][j] + count[i][j-1]
    return count[m-1][n-1]

"""
ints = [1, 0, 0, 1, 0, 0, 1, 0 ]
# the following code will not work is all 1, 1,
#import sys
#ints = [0]
#max_value = -sys.maxint
def flip(line):
    value, max_value, ptr, ret = 0, 0, 0, []
    for i in range(len(line)):
        value += (line[i] == 0) * 2 - 1
        print "Value: ", value, " at i : ", i

        if value < 0:
            value, ptr = 0, i + 1
        elif value > max_value:
            max_value, ret = value, [ptr, i]

    return ret
result =  flip(ints)
print result
wL, wR = result[0], result[1]
one1 = filter(lambda x: x == 1, ints[0:wL])
one2 = filter(lambda x: x == 0, ints[wL:wR + 1])
one3 = filter(lambda x: x == 1, ints[wR:])
print one1, one2, one3
print len(one1) + len(one2) + len(one3)


"""
ANALYSIS

The string must can be separated into several segments:

[0*][1+][0+][1+] ... [1+][0*]
If we choose L and R to be the answer, we are sure about the following truth:

count(0) - count(1) must be the largest among all choice of L and R.
L must be the start of one of [0+] or [0*] segment.
R must be the end of one of [0+] or [0*] segment.
We start counting from the start of the string with the iteration of each segment:

init a variable, say value to be 0, and a ptr which points to 0
add x to value if the segment has x '0's
minus x from value if the segment has x '1's
every time the value becomes smaller than 0, reset it to be 0. Also set ptr to be the current position
if value is larger than it ever had been, record the current value and the corresponding L and R.
Time complexity: O(n)
Space complexity: O(1)

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = raw_input('')
ints = raw_input('')
ints = ints.split()

def flip(line):
    value, max_value, ptr, ret = 0, 0, 0, []
    for i in range(len(line)):
        value += (line[i] == '0') * 2 - 1
        if value < 0:
            value, ptr = 0, i + 1
        elif value > max_value:
            max_value, ret = value, [ptr, i]
    return ret
result =  flip(ints)
wL, wR = result[0], result[1]
one1 = filter(lambda x: x == '1', ints[0:wL])
one2 = filter(lambda x: x == '0', ints[wL:wR + 1])
one3 = filter(lambda x: x == '1', ints[wR:])
print len(one1) + len(one2) + len(one3)
"""

"""
Problems
1.) BooHoo (Coding Challenge)
If number if divisible by 3 then "BOO", if by 5 then "HOO" by both then "BOOHOO"

2.) Inversed Number (Coding Challenge)
    Complement the number 1 -> 0 and 0 -> 1

3.) J Delta (Coding Challenge) : i + D, i - D
Simple problem if gievn a delta you have numbers such that they are D distance apart.

4.) Routes in a matrix (Coding Challenge)
Given a matrix with 1's and 0's how many ways are there to reach the bottom rightmost corner.

4.) bit Flip in L, R
given an array of 1 and 0. You have to flip bits of a range(L, R) such that the number of 1's are maximized in that array.

"""