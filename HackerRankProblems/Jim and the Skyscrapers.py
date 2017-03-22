__author__ = 'deepika'




n = int(raw_input())

arr = raw_input()
arr = arr.split()

matrix = [ [0 for _ in range(n)] for i in range(n)]

result = list()

#for i in range(n):
#    matrix[i][i] = 1

for length in range(2, n+1):
    for i in range(n):
        #print " i = ", i, " j = ", len + i - 1
        j = length + i - 1
        if (j >= n):
            continue
        if (length == 2):
            if ( arr[i] == arr[j]):
                matrix[i][j] = 1
                result.append((i+1, j+1))
        elif(length == 3):
            if (arr[i] == arr[j] and arr[i] > arr[i+1]):
                matrix[i][j] = 1
                result.append((i+1, j+1))
        else:
            if (length % 2 != 0): #Odd
                if (matrix[i+1][j-1] == 1 and arr[i+1] < arr[i]):
                    matrix[i][j] = 1
                    result.append((i+1, j+1))
            else:
                if (matrix[i][j-1] == 1 and arr[j-1] == arr[j]):
                    matrix[i][j] = 1
                    result.append((i+1, j+1))
print str(len(result) * 2)