
"""
Subaarray of less than equal to k
"""

def maxLength(a, k):
    results = []

    max_so_far = 0
    max_ending_here = 0
    i = 0
    while( i < len(a)):
        max_ending_here = max(0, max_ending_here + a[i])
        if (max_ending_here >= max_so_far and max_ending_here <= k):
            max_so_far = max(max_so_far, max_ending_here)
            results.append(max_so_far)
            i = i + 1
            continue
        else:
            max_ending_here = 0
            max_so_far = 0
            #start from the same i hwere the k was exceeed
    return max(results)



if __name__ == "__main__":
    arr = [1, 2, 3]
    print maxLength(arr, 4)