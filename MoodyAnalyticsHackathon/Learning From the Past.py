


if __name__=="__main__":
    n = int(raw_input(''))
    result =[]
    for i in range(0,n):
        line = raw_input('');
        line = line.split()
        line = sorted(line,reverse=True)
        #print line
        max1 = line[0]
        max2 = line[1]
        result.append(int(max1)+int(max2))
        #print "Updated result : ", result
    print max(result)