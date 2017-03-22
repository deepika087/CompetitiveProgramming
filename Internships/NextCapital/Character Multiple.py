__author__ = 'deepika'
def countCharacters( strings,  multiples):

    result = []
    for i in range(len(strings)):
        string = strings[i]
        multiple = multiples[i]
        dictionary = dict()
        count = 0
        for item in string:
            if (dictionary.get(item, -1) == -1): #Not present
                dictionary[item] = 1
            else:
                dictionary[item] = dictionary[item] + 1

        for (k, v) in dictionary.items():
            if (v%multiple == 0):
                count = count + 1
        result.append(count)
    print result

if __name__=="__main__":
    strings = ['aaabbdaaekhfjkcbks', 'askJSKWIUQEBSK']
    multiples = [5, 2]

    print countCharacters(strings, multiples)



