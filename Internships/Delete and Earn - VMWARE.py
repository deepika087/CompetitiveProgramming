# Complete the function below.
# 8 pass of 14 some had time exception

"""
you have to maximumize points such that when when u burst ai ai - 1 and ai + 1 are automatically burst.
Now by bursting such ai gather points.
Second idea could have been sorting in descending order. Burst first one. while next elements are ai + 1 then ignore that.
My assumption is correct solution is greedy but cann't be sure.
"""
def maxPoints(elements):

    result = 0
    while(len(elements) > 0):
        max_iteration = max(elements)

        elements.remove(max_iteration)
        elements = list(filter(lambda x: x != max_iteration + 1 , elements))
        elements = list(filter(lambda x: x != max_iteration - 1 , elements))
        result = result + max_iteration
    return result

maxPoints([1, 2, 1, 3, 2, 3])
maxPoints([3, 3, 4, 2])

