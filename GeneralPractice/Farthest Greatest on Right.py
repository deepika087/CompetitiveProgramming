__author__ = 'deepika'


"""
Almost like https://www.geeksforgeeks.org/find-the-farthest-smaller-number-in-the-right-side/
But the suffix min idea will not work here because pre condition for BS is sorted array.
And if I create a suffix max then that won't be satisfied.


My approach is that I combined sliding window and binary search algo.
The idea is that start from the end. Now, if the incoming element is greater than
top of the stack then simply put it to stack.

Bottom of the stack represents farthest element, now whether is that farthest element is greater than A[i]
or not is the question.

If the incoming element is less than bottom of stack. then this is the farthest element greater than A[i]
Otherwise do a binary search on the stack.

Time: O(n log n) as you might have to do binary search n number of times on the stack.
"""

class Solution:

    def farthestGreatest(self, A):

        if len(A) == 0 or len(A) == 1:
            return []

        stack = []
        result = [-1 for i in range(len(A))]

        for i in range(len(A)-1, -1, -1):
            if len(stack) == 0:
                stack.append(i)

            elif A[i] > A[stack[-1]]:
                stack.append(i)

            elif A[i] < A[stack[0]]: # if the farthest element is greater than we are good.
                result[i] = A[stack[0]]
            else:
                low = 0
                high = len(stack) - 1

                while low >= 0 and high < len(stack) and low <= high:
                    mid = (low + high)/2

                    if (A[stack[mid]] < A[i] ):
                        low = mid + 1
                    else:
                        result[i] = A[stack[high]]
                        high = mid - 1
        #print(result)
        return result



s=Solution()
assert s.farthestGreatest([21, 5, 6, 56, 88, 52]) == [ 52, 52, 52, 88, -1, -1]
assert s.farthestGreatest([21, 21, 21, 21, 88, 52]) == [ 52, 52, 52, 52, -1, -1]
assert s.farthestGreatest([21, 5, 6, 56, 88, 52,53]) == [ 53, 53, 53, 88, -1, 53, -1]
assert s.farthestGreatest([1, 2, 3, 4, 5, 6]) == [ 6, 6, 6, 6, 6, -1]
assert s.farthestGreatest([6, 5, 4, 3, 2, 1]) == [ -1, -1, -1, -1, -1, -1]
assert s.farthestGreatest([10, 20, 15, 18]) == [ 18, -1, 18, -1]
assert s.farthestGreatest([10, 20, 8, 9]) == [ 20, -1, 9, -1]
