

"""
402. Remove K Digits

Also
Zappos Coding challenge
given a number in string format say something ike 1234089389 and number n = number of elements u can delete
find the smallest possible number you can make out of these.
"""
def attempt2(s, n):
    N = len(s)
    targetLen = N - n
    result = ''
    while(targetLen != 0):
        min_so_far = min(s[0:n+1])
        result = result + min_so_far
        s = s[s.index(min_so_far) + 1 :]
        targetLen = targetLen - 1
        n = len(s) - targetLen
    i = 0
    while(i < len(result) and ord(result[i]) == ord('0')):
        i = i + 1
    if (len(result[i:]) == 0):
        return "0"
    else:
        return result[i:]

if __name__=="__main__":
    s = "10";
    n = 2
    if (n >= len(s)):
        print "0"
    elif (n == 0):
        print s
    else:
        print attempt2(s, n)