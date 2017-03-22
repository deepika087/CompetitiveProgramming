

# 1. If i is a multiple of 2 and i is greater than 0,
#      array[i] = array[i] + array[i - 1]
# 2. If i is a multiple of 3 and i is greater than 0 and i + 1 < L,
#      Swap array[i] and array[i + 1]
# 3. If i is a multiple of 5 and i is greater than 0,
#      array[i] = array[i] * 2
# 4. If i is a multiple of 7 or when no other rules apply,
#      array[i] = array[i] - 1
#
# __author__ = 'deepika'


def processArray(array):
    result = [0 for i in range(len(array))]

    for i in range(len(array)):
        applied=False
        if (i%2==0 and i > 0):
            array[i] = array[i] + array[i-1]
            applied=True
        if (i%3==0 and i > 0 and i+1 < len(array)):
            array[i+1], array[i] = array[i], array[i+1]
            applied=True
        if (i%5==0 and i > 0):
            array[i] = array[i]*2
            applied=True
        if(i%7==0 or not applied):
            array[i] = array[i] - 1
    return array
if __name__=="__main__":
    array = [1,2 ,3 ,4 , 5,6]
    print processArray(array)
    array = [0, 1,2 ,3 ,4 ]
    print processArray(array)