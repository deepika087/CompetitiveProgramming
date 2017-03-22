
"""
Almost like a state machine. DUp mean duplicate the element and POP means pop the element and so on.
"""

def solution(S):
    LIMIT = 2**20 - 1

    S = S.split()
    stack = []

    for item in S:
        #print "processing item = ", item
        if (item in ["DUP", "POP", "+", "-"] ):
            if (len(stack) == 0):
                return -1;
            else:
                if (item == "DUP"):
                    lastValue = stack.pop(-1)
                    stack.append(lastValue)
                    stack.append(lastValue)
                    #print " Stack after duplication = ", stack
                elif (item == "POP"):
                    if (len(stack) == 0):
                        return -1
                    stack.pop(-1)
                    #print " Stack after POP = ", stack
                elif (ord(item) == ord('+')):
                    if (len(stack) == 0):
                        return -1
                    val1 = stack.pop(-1)
                    if (len(stack) == 0):
                        return -1
                    val2 = stack.pop(-1)
                    stack.append((val1 + val2)%LIMIT)
                    #print " Stack after addition = ", stack
                else:
                    if (len(stack) == 0):
                        return -1
                    val1 = stack.pop(-1)
                    if (len(stack) == 0):
                        return -1
                    val2 = stack.pop(-1)
                    stack.append((val1 - val2))
                    #print " Stack after subtraction = ", stack

        else:
            stack.append(int(item)%LIMIT)
            #print " stack = ", stack
    result = stack.pop(-1)
    return result if result > 0 else -1


if __name__ == "__main__":
    S = "13 DUP 4 POP 5 DUP + DUP + -"
    print solution(S)
    S = "3 DUP 5 - -"
    print solution(S)
    S = "5 6 + -"
    print solution(S)