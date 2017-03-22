

import copy
def get_median(buffer, D):
    if (D%2 == 0) : #even
        return (buffer[D/2] + buffer[(D-1)/2])/2.0
    else:
        return (buffer[D/2])

def getNotifications(N, D, numbers):
    notifications = 0

    buffer = numbers[0:D]
    skipSort = False

    for i in numbers[D:]:
        #print " Buffer before ", buffer
        if not(skipSort):
            temp_buffer = sorted(buffer)
        else:
            temp_buffer = copy.copy(buffer)

        #print " Buffer after sorting ", buffer
        median = get_median(temp_buffer, D)
        if ( i >= 2 * median):
            notifications = notifications + 1
        buffer.pop(0)

        if ( i >= buffer[-1]):
            buffer.append(i)
            skipSort = True
        elif ( i < buffer[0]):
            buffer = [i] + buffer
            skipSort = True
        else:
            buffer.append(i)
            skipSort = False
        print " Buffer after adjusting is " ,buffer

    return notifications

def getInput():
    ND = raw_input('')
    N = int(ND.split()[0])
    D = int(ND.split()[1])

    numbers = raw_input('')
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]

    return N, D, numbers

if __name__ == "__main__":


    N, D, numbers = getInput()

    print getNotifications(N, D, numbers)

    """
    N = 9
    D = 5
    numbers = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    print getNotifications(N, D, numbers)

    print " Run 2 :"
    N = 5
    D = 4
    numbers = [1, 2, 3, 4, 4]
    print getNotifications(N, D, numbers)
    """

