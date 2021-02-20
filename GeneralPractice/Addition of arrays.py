__author__ = 'deepika'


arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 3, 1, 4]

sumT = 0
for _ in (arr1 + arr2):
    sumT ^= _

print sumT