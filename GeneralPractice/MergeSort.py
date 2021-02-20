__author__ = 'deepika'


def mergeSort(data):

    left = 0
    right = (len(data) - 1) /2
    return mergeSortUtil(left, right, data)

def mergeSortUtil(left, right, arr):
    if left > right:
        return
    if left == right:
        return arr

    mid = right - (right - left)/2

    leftArr = mergeSortUtil(left, mid, arr)
    rightArr = mergeSortUtil(mid + 1, right, arr)

    return merge(leftArr, rightArr)

def merge(leftArr, rightArr):

    i, j = 0, 0
    result = [0] * (len(leftArr) + len(rightArr))
    k = 0

    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            result[k] = leftArr[i]
            k += 1
            i += 1
        elif leftArr[i] > rightArr[j]:
            result[k] = rightArr[j]
            k += 1
            j += 1
        else:
            result[k] = leftArr[i]
            k += 1
            result[k] = rightArr[j]
            k += 1
            i += 1
            j += 1


    while i < len(leftArr):
        result[k] = leftArr[i]
        k += 1
        i += 1

    while j < len(rightArr):
        result[k] = rightArr[j]
        k += 1
        j += 1
	return result


print(mergeSort([3, 6, 1, 5, 8, 7, 2]))
