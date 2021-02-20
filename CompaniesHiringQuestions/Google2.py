__author__ = 'deepika'

# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"


def solution(S):
    # write your code in Python 2.7
    disitinctElement = set()
    for i in range(len(S)):
        if S[i] in disitinctElement or S[i] == ":":
            continue
        else:
            disitinctElement.add(S[i])

    disitinctElement = list(disitinctElement)
    result = permuteK(disitinctElement, 4)
    result = sorted(result)
    result = list(filter(lambda x: x >= '0000' and x <= '2359', result))

    print result
    S = S.replace(':', '')
    index = result.index(S)
    if index == len(result) - 1:
        inFormat(result[0])
    else:
        inFormat(result[index+1])
    #print "Entire set:", result

def inFormat(S):
    result = []
    for i in range(len(S)):
        if i == 2:
            result.append(':')
        result.append(S[i])

    print ''.join(result)
# Python function to print permutations of a given list
def permuteK(setInput, k) :
    n = len(setInput)
    resultSet = []
    printAllKLengthRecprintAllKLengthRec(setInput, "", n, k, resultSet)
    return resultSet

def printAllKLengthRecprintAllKLengthRec(setInput, prefix, n, k, resultSet) :

    if (k == 0):
        resultSet.append(prefix);
        return;

    #// One by one add all characters from set and recursively
    #// call for k equals to k-1
    for i in range(n):
        newPrefix = prefix + str(setInput[i])
        printAllKLengthRecprintAllKLengthRec(setInput, newPrefix, n, k - 1, resultSet);

#solution("23:59")
#solution("11:00")
#solution("11:07")
#solution("19:34")
solution("20:48")