

def check_log_history( events):
    stack = list();
    ptr = 0;
    for index, item in enumerate(events):
        event = item.split()
        if (event[0] == "ACQUIRE"):
            if (int(event[1]) in stack):
                return index+1
            stack.append(int(event[1]))
        elif event[0] == "RELEASE":
            if (len(stack) == 0):
                print index+1
                return;
            topEle = stack.pop()
            if (topEle != int(event[1])): #Error occured
                print index+1

    if (len(stack) > 0):
        print len(events)+1
    else:
        print "0"

def is_palin(input):
    left = 0
    right = len(input)-1
    isPalin=True;
    while(left <= right):
        if (ord(input[left]) != ord(input[right])):
            isPalin = False
            break;
        else:
            left = left + 1;
            right = right - 1;
    return isPalin

def count_palindromes(S):
    result = 0;
    result = result + len(S);

    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if (is_palin(S[i:j+1]) == True):
                #print "Found", S[i:j+1]
                result = result  + 1
    return result
if __name__=="__main__":
    events = {
        "ACQUIRE 364",
        "ACQUIRE 84",
        "RELEASE 84",
        "RELEASE 364"
        }
    #check_log_history(events)

    count_palindromes("wowpurerocks")