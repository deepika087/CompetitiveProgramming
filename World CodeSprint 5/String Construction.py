

if __name__=="__main__":
    T = int(raw_input(''))
    for i in range(T):
        s = raw_input('')
        ptr = 0
        cost = 0
        target_s = ""
        while(ptr < len(s)):
            if ptr == 0:
                target_s = s[ptr]
                cost = cost + 1 # copy the first character as it is
                ptr = ptr + 1
            else:
                if (s[ptr] not in target_s ):
                    target_s = target_s + s[ptr]
                    ptr = ptr + 1;
                    cost = cost + 1
                    #print "Target String = ", target_s, " With cost = ", cost
                else: # this is candidate for copy substring
                    end = ptr + 2
                    #print "Verifying ", s[ptr:end]
                    while(s[ptr:end] in target_s and end < len(s)):
                        end = end + 1

                    end = end - 2
                    target_s = target_s + s[ptr:end+1]
                    ptr = end + 1
                    #print "Target String = ", target_s, " With cost = ", cost
        print cost