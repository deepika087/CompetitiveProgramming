__author__ = 'deepika'
from itertools import groupby


inputList =  [ (5,1), (7,4), (1,7,4), (2,4,6,1) ]

print "Input: ", inputList

finalResult = []
for key, group in groupby(inputList, lambda x: len(x)):
    for thing in group:
        finalResult.append(sorted(thing))
        #print thing, key

finalResult = list(map(lambda x: tuple(x), finalResult))
print "Output: ",  finalResult