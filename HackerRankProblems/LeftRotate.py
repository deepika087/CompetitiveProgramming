
import collections

def rotate(arr, d):
    arr = collections.deque(arr)
    arr.rotate(-d)
    #print type(arr)
    return arr

if __name__ =="__main__":
    dn=raw_input()
    dn=dn.split()
    n=int(dn[0])
    d=int(dn[1])

    arr=raw_input()
    arr=list(arr)
    arr = list(rotate(arr, d))

    result = ""
    for item in arr:
        if (item == ' '):
            continue
        else:
            if (result == ""):
                result = str(item) + " "
            else:
                result = result + str(item) + " "
    print result.strip()
