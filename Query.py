"""
Someone asked me to write this code that is supper generic to parse nay list/set/tuple
"""
__author__ = 'deepika'


input1 =  [ (('162', 'M'), 4.0),
            (('1372', 'F'), 4.0),
            (('1917', 'M'), 3.0)
        ]

input2 = [ (['162', 'M'], 4.0),
            (['1372', 'F'], 4.0),
            (['1917', 'M'], 3.0)
        ]

input3 = [ ([10, 20, 30], 1), ((40, 50, 60), 2), ([(70, 80), 100], 3)]

input4 = [ ([10, 11], (12, 13), 1), ([(14, 15), 16], 2, 3), ((17, [18, 19]), 4)]
outputExpected = [  ['162', 'M', 4.0],
                    ['1372', 'F', 4.0],
                    ['1917', 'M', 3.0]
                ]


def parseDS(setOrList):

    temp = []
    for i in range(len(setOrList)):
        _inp = setOrList[i]
        if isinstance(_inp, tuple):
            temp += parseDS(_inp)
        elif isinstance(_inp, list):
            temp += parseDS(_inp)
        else:
            temp.append(_inp)
    return temp

def parseFunc(input):
    result = []
    for _inp in input:
        _r = []
        for i in range(len(_inp)):
            #print "Eval: ", _inp[i]
            if isinstance(_inp[i], (list, tuple)):
                _r +=(parseDS(_inp[i]))
            else:
                _r.append(_inp[i])
        result.append(_r)
    return result

if __name__ == "__main__":
    assert parseFunc(input1) == outputExpected
    assert parseFunc(input2) == outputExpected
    assert parseFunc(input3) == [[10, 20, 30, 1], [40, 50, 60, 2], [70, 80, 100, 3]]
    assert parseFunc(input4) == [[10, 11, 12, 13, 1], [14, 15, 16, 2, 3], [17,18, 19, 4]]
