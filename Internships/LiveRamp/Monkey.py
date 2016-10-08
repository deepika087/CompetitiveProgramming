"""
This is the question which was actually asked in LiveRamp coding challenge.
"""
def solution(A, D):
    dest = len(A) # this is N
    curr = -1

    if (D > dest):
        return 0
    for time in range(0, max(A)+1):
        if (time in A): #this will filter -1
            #find the stone position which is now visible
            stone = A.index(time) 
            if (curr == -1 and stone <= D):
                curr = stone
            elif (stone <= curr):
                continue #No point of this stone
            elif (stone-curr <= D): #forgot to add in the main solution
                curr = stone
            if (dest - curr <= D):
                return time
        else:
            continue;
    return -1


if __name__ =="__main__":
    print solution([1, -1, 0, 7, 3, 6, 8, 11, 18], 3)