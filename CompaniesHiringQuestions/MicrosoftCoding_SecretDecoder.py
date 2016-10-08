
"""
Microsoft coding challenge
Accepted Solution
"""

if __name__=="__main__":
    mapping = raw_input('')
    line = raw_input('')
    mappings = mapping.split()
    trueMapping = {};
    for item in mappings:
        splitItem = map(lambda c: c.upper(), item)
        trueMapping[splitItem[0]] = splitItem[2]

    print trueMapping

    result = ''
    for item in line:
        if ord(item) >= 65 and ord(item) <= 90: #Uppercase
            if (trueMapping.get(item, -1) != -1):
                result = result + trueMapping.get(item)
        elif (ord(item) >= 97 and ord(item) <= 122): #encountered lower case
            itemUpper = item.upper()
            if (trueMapping.get(itemUpper, -1) != -1):
                result = result + trueMapping.get(itemUpper).lower()
        else:
            result = result + item;

    print result