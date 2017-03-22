

def checkIfInavlid(inputLine):
    if inputLine[0] == '*' or inputLine[len(inputLine)-1] == '*':
        return False

    for i in range(0, len(inputLine)):
        if (inputLine[i] == '*' and i+1 < inputLine and i+2 <= inputLine):
            if (inputLine[i+1] == '*' and inputLine[i+2] == '*'):
                return False
    return True

if __name__=="__main__":
    modulus = 10**9 + 7

    T = int(raw_input(''))
    for i in range(T):
        inputLine = raw_input('')

        multiPliLine = []
        if (checkIfInavlid(inputLine) == False):
            print "Syntax Error"
        else:
            i = 0
            n = len(inputLine)
            result = 0
            while ( i < n and i != n-1):
                prev = int(inputLine[i]);
                #print "At i =", i, "with prev set to = ", prev
                while not( i != n-1 and i+1 < n and i+2 < n and inputLine[i+2] >= '0' and inputLine[i+2] <= '9'):
                    print "At i = ", i, " will be raising to the power = ", inputLine[i+3]
                    if ( i == n or i == n-1):
                        break
                    a = prev % modulus
                    b = int(inputLine[i+3]) % modulus
                    result = ( a  **  b) % modulus
                    prev = result
                    i = i + 3

                if (prev != int(inputLine[i])):
                    print "I am here"
                    multiPliLine.append(prev)
                    print multiPliLine

                while ( i + 1 < n and inputLine[i+2] >= '0' and inputLine[i+2] <= '9' ):
                    print " I value = ", i
                    if (i == 0):
                        multiPliLine.append(int(inputLine[i]))
                        #multiPliLine.append(int(inputLine[i+2]))
                        print "Appending", inputLine[i], " to multiplication list"
                    else:
                        multiPliLine.append(int(inputLine[i+2]))
                        print "Appending<>", inputLine[i+2], " to multiplication list"
                    print multiPliLine
                    i = i + 2

            print multiPliLine
            print reduce(lambda x,y: x*y, multiPliLine)


