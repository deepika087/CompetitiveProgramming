"""
Microsoft coding challenge
Accepted solution
"""

if __name__ =="__main__":

    lines = [line.rstrip('\r\n') for line in open('/Users/deepika/Desktop/MicrosoftExam/_3/PracticeInput.txt')]
    for line in lines:
        line = line.split(',')
        #print "line = ", line
        ndisk = line[0]
        fromPeg = line[1]
        toPeg = line[2]
        result = []
        if fromPeg == toPeg:
            print "0"
        else:
            print pow(2,int(ndisk)) - 1
