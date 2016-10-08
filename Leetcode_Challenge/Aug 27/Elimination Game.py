import numbers
def call_func(n):
    nList = list()
    for x in range(1, n+1):
        nList.append(x)
    #print nList

    removeStart = True;
    while len(nList) != 1:
        if (removeStart):
            nList = nList[1::2]
            #print nList
            removeStart = False
        else:
            if (len(nList) % 2 != 0): #ODD
                nList = nList[1::2]
                #print nList
            else: #even
                nList.reverse();
                nList = nList[1::2];
                nList.reverse()
                #print nList
            removeStart = True
    return nList[0]


def new_Calc(n):
    if n == 1:
        return 1;
    elif ( n == 2 or n == 3 or n == 4 or n ==5 ):
        return 2;
    elif (n == 6 or n == 7):
        return 4
    else:
        if (n % 2 != 0): #Odd
            n = n-1

        seed = 8
        notfound = True;
        while (seed < n):
            seed = seed + 4
            #print "seed = ", seed
        if (seed == n):
            return 6;
        else:
            return 8;

if __name__=='__main__':
    #n = int(raw_input(''))
    #call_func(int(n))
    for i in range(10, 100):
        print i, " --> ", call_func(int(i))

    #print (new_Calc(int(n)))


