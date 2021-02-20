__author__ = 'deepika'


def solution(inputTable):

    #Am, Mex, Seafood
    dictionary = {}
    specialities = set()
    for line in inputTable:
        if line[0] not in dictionary:
            dictionary[line[0]] = {}

        if line[1] not in dictionary[line[0]]:
            dictionary[line[0]][line[1]] = line[2]
            specialities.add(line[1])
        else:
            dictionary[line[0]][line[1]] += line[2]

    sortedKeys = sorted(dictionary)
    specialities = sorted(specialities)
    print(sortedKeys)
    print(specialities)

    result = []
    for k in sortedKeys:
        line = []
        city = dictionary[k]

        for sp in specialities:
            if sp in city:
                line.append(int(city[sp]))
            else:
                line.append(0)
        result.append(line)
    return result


string = [
    [ "Boston", "Mexican", "163"],
    [ "Boston", "Seafood", "194"],
    [ "Boston", "Smoothie", "14"],
    [ "Los Angeles", "American", "1239"],
    [ "Los Angeles", "Mexican", "1389"],
    [ "Los Angeles", "Seafood", "556"],
    [ "Los Angeles", "Burger", "5"],


]
print(solution(string))