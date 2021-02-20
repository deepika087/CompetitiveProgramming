__author__ = 'deepika'

arr = [3, 2, 6, 5, 8, 2, 9]
result = [ 0 for i in range(len(arr))]

for i in range(0, len(arr)):
	result[i] = 0
	for j in range(i - 1, -1 , -1):
		if arr[j] < arr[i]:
            result[i] = arr[j]
            break

print(result)
