l"""
Zappos coding challenge
Input  : ABC    DEF
Output : FED    CBA

"""

"""
won't work because in Python we cannot assign char to string for ex
s[i] = 1 is invalid in python. Use replace instead. The same has been done in attempt2
"""
def reverse(s):
    start = 0;
    end = 0;
    while(end < len(s)):
        while(end + 1 < len(s) and s[end+1] != ' '):
            end = end + 1
        # at this point we have end and start at proper  positions
        left = start
        right = end

        while(left <= right):
            temp = s[left]
            s[right] = s[left]
            s[left] = temp

            left = left + 1;
            right = right - 1
        while (s[end + 1 ] == ' ' and end < len(s)):
            end = end + 1;
        start = end + 1;
        end = start

def attempt2(s):
    start = 0
    end = 0
    while(end < len(s)):
        while(s[end+1] != ' '): #(end + 1 < len(s) and
            end = end + 1
        # at this point we have end and start at proper  positions
        left = start
        right = end

        s.replace(s[left:right+1], s[left:right+1:-1], 1) #just one instance replace

        while (end + 1 < len(s) and s[end + 1 ] == ' '  ):
            end = end + 1;
        start = end + 1;
        end = start
    print (s)

if __name__=="__main__":
    s = raw_input('');

    #print reverse(s)
    attempt2(s)