"""
Zappos coding challenge

Given two arrays. find if the there are two elements in batteryOne,batteryTwo such that
sum of the two is target
"""

if __name__=="__main__":
    batteryOne = raw_input('')
    batteryTwo = raw_input('')
    target = int(raw_input(''))

    batteryOne = [ target - int(x) for x in batteryOne.split()]
    batteryTwo = [ int(x) for x in batteryTwo.split()]

    s = filter(lambda x : x in batteryTwo, batteryOne)
    if len(s) > 0:
        print "True"
    else:
        print "False"

