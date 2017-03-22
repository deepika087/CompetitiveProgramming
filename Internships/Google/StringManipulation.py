
"""
There are licence keys such as A-BCDEF-GEF. Given K you have to return string such .....-FED-GEF
First group may have less than k elements but each other group should have k elements
"""
def solution(S, K):
    result = []
    i = len(S) - 1

    slice = K
    while (i >= 0):
        part = []
        while (slice > 0 and i >= 0):
            if (ord(S[i]) != ord('-') ):
                part.insert(0, (S[i].upper()))
                slice = slice - 1
                i = i - 1
            else:
                i = i - 1
        slice = K
        result.insert(0, (''.join(part)))
    #result = reversed(result)
    return '-'.join(result)

if __name__ == "__main__":
    S = "2-4A0r7-4k"
    K = 3
    print solution(S, K)

    K=4
    print solution(S, K)

    K=2
    print solution(S, K)

    S="r"
    K=1
    print solution(S, K)