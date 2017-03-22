

def findDiffPair(arr, left , right, sum):
    # Initialize positions of two element

    # Search for a pair
    if ( sum in arr):
        return True

    if ( sum < 0):
        pass
    while left <= right:

        if arr[right]-arr[left] == sum:
            return True

        elif arr[right] - arr[left] < sum:
            return findDiffPair( arr, left + 1, right, sum - arr[left] ) or findDiffPair(arr, left, right, sum - A[left])
        else:
            right = right - 1
    return False

def hasSumEqual(A, left, right, sum):
    if ( sum in A):
        return True
    if ( sum == 0):
        return True
    if ( sum < 0):
        return False

    while left < right:
        if (A[left] + A[right] == sum):
            return True
        elif (A[left] + A[right] < sum):
            return hasSumEqual( A, left + 1, right, sum - A[left] ) or hasSumEqual(A, left, right, sum - A[left])
        else:
            return hasSumEqual( A, left, right - 1, sum - A[right] ) or hasSumEqual(A, left, right, sum - A[right])

    return False

if __name__ == "__main__":
    N = int(raw_input(''))
    numbers = raw_input('')
    numbers = numbers.split()
    numbers = [ int (x) for x in numbers]
    targets = []

    M = int(raw_input(''))
    targets = raw_input('')
    targets = targets.split()
    targets = [ int(x) for x in targets]

    numbers = sorted(numbers)
    for j in targets:

        if ( findDiffPair(numbers, 0, len(numbers) - 1, j) == True):
            print "yes"
            continue
        else:
            if ( hasSumEqual(numbers, 0, len(numbers) - 1, j) == True):
                print "yes"
                continue
            else:
                print "no"