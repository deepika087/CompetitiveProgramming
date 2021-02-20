__author__ = 'deepika'


#Max subarray with sum lees than equal to k

import sys
def maxLength(a, k):

    cur_sum = a[0]
    max_len = 1
    start = 0

    for i in range(1, len(a)):
        while cur_sum > k and start < i:
            cur_sum -= a[start]
            start = start + 1

        if cur_sum <= k:
            max_len = max(max_len, i - start)

        cur_sum = cur_sum + a[i]

    if cur_sum <= k:
        max_len = max(max_len, i - start + 1)

    return max_len


print maxLength([3,1,2,1], 4)
#print maxLength([1,2,3 ], 4)