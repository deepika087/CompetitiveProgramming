__author__ = 'deepika'


def shortestWinterLength(listofTemperatures):

    if len(listofTemperatures) == 0 :
        return 0

    length = len(listofTemperatures)
    winter_high = listofTemperatures[0]
    overall_high = listofTemperatures[0]
    winter_length = 0

    # Get max in the left array
    for temperature in listofTemperatures:
        if temperature <= winter_high :
            winter_high = overall_high
        elif temperature > overall_high :
            overall_high = temperature
        print("winter_high = " + str(winter_high) + " overall_high = " + str(overall_high))

    # count all the values which are less than max in left array
    for temperature in listofTemperatures :
        if temperature <= winter_high :
            winter_length += 1

    # total length of the left array
    print (winter_length)

shortestWinterLength([5, -2, 3, 8, 6])
shortestWinterLength([-5, -5, -5, -42, 6, 12])