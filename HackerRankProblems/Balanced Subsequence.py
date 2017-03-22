
"""
Sears Dots and Arrow
Balanced Subsequence

All Test cases passed
"""

def getBalancedSubSequence(S):
    stack = []
    i = 0
    while(S[i] == ')'):
        i = i + 1

    #Now I have the first place where S[i] = '('
    if ( i == len(S) - 1):
        return 0
    result = 0
    for item in S[i:]:
        if (item == '('):
            stack.append(item)
        elif (item == ')'):
            if (len(stack) > 0 and stack.pop(-1) == '('):
                result = result + 2 # becuase each () will count for 2 rather than 1 balanced pair
            #Else ignore this
    return result


def inputs():
    SList = []
    T = int(raw_input(''))
    for i in range(T):
        S = raw_input('')
        SList.append(S)
    return SList

if __name__ =="__main__":
    SList = inputs()
        #['()())', '))))(((', '()(((((()']
        #

    for S in SList:
        print getBalancedSubSequence(S)


