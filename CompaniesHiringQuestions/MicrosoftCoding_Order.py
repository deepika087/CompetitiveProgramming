
"""
Microsoft coding challenge
"""
def doItAgian(lines):
    N = int(lines[0])
    count = 1
    lost = []
    for item in lines[1:]:
        s_ = filter(lambda c: c == 'W', line)
        if (len(s_) == 0):
            lost.append(count)

if __name__=="__main__":
    lines = [line.rstrip('\r\n') for line in open('/Users/deepika/Desktop/MicrosoftExam/_4/PracticeInput.txt')]

    print lines
    #doItAgian(lines)
    N = int(lines[0])
    #print N
    trueMapping = dict()
    count = 1;
    for line in lines[1:]:
        s_ = filter(lambda c: c == 'W', line)
        trueMapping[count] = len(s_)
        count = count + 1

    print trueMapping
    result = []
    for w in sorted(trueMapping, key=trueMapping.get, reverse=True):
        result.append(str(w))

    print ' '.join(result)

