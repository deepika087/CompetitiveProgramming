"""
Find maximum substring such that it is in AP
"""


def solution(A):
    start = 0
    end = 1
    result = 0
    while(start < len(A)):
        while(end + 1 < len(A) and (A[end] - A[end-1] == A[end+1] - A[end])):
            end = end + 1
        if (end - start == 2):
            #print " Found at start = ", start , " and end = ", end
            result = result + 1
        elif (end - start > 2):
            #print " Found at start = ", start , " and end = ", end
            result = result + 2 * (end - start - 2) + 1
            if ( result > 10**9):
                return -1
            #print " New result = ", result
        start = end
        end = end + 1
    return result


if __name__=="__main__":
    print solution([-1, 1, 3, 3, 3, 2, 1, 0] )
    print solution([-2, 4, 2, 0] )