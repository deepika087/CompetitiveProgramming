

if __name__=="__main__":
    s = raw_input('')
    t = raw_input('')

    sList = list(s)
    tList = list(t)
    for item in sList:
        if (item in tList):
            tList.remove(item)
            #print "Updated t = ", tList
    print tList[0]