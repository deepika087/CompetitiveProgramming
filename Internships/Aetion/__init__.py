

"""
Find the minimum difference between two elements.
This is wrong becuase if array is -100, -1, 0
My solution will return 99 where as correct answer is 1
"""
def solution(A):

    A = sorted(A)
    print A

if __name__=="__main__":
    A = [8, 24, 3, 20, 1, 17]
    print solution(A)