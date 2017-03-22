

if __name__ == "__main__":
    line = raw_input('')
    N = int(raw_input(''))

    toggle = True
    i = 0

    result = []
    if ( N == 1):
        print line
    elif ( N > len(line)):
        print line[::-1]
    else:
        while (i < len(line)):
            if (toggle):
                start = i
                end = i + N-1
                portion = list(line[start:end + 1])
                portion.reverse()
                reverse = "".join(portion)
                #print "start = ", start, " end = ", end
                result.append(reverse)
                toggle = False
                i = i + N
            else:
                start = i
                end = i + N - 1
                toggle = True
                #print "start = ", start, " end = ", end
                result.append(line[start:end + 1])
                i = i + N

        #print result
        print "".join(result)