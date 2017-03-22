


def balancePoint(arr):

    sumLeft = 0
    for i in range(len(arr)):
        sumLeft = sumLeft + arr[i]

    sumRight = arr[len(arr) - 1];
    sumLeft = sumLeft - arr[len(arr) - 1]
    for i in range(len(arr) - 2, -1, -1):
        if (sumRight == sumLeft - arr[i]):
            return i

        sumRight = sumRight + arr[i]
        sumLeft = sumLeft - arr[i]

    return -1;

if __name__=="__main__":
    print balancePoint([1, 2, 3, 3])

    #arr[0], arr[1], arr[2], arr[3]