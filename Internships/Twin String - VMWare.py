

"""
There are two strings. say A and B. There are two functions
swapWithOdd: that replaces odd index character in A with an odd index character of B
swapWithEven: that replaces even index character in A with an even index character of B.

You have to tell if it possible to transform A to B
"""
def process_wrong_solution(a, b):
    if (len(a) != len(b)):
        return "No"

    for i in range(len(a)):
        if (a[i] not in b):
            return "No"
        if (i % 2 == 0 and any((j % 2 == 0 and b[j] == a[i]) for j in range(len(a)))): #Odd
            continue
        if (i % 2 and any(( (j % 2 and b[j] == a[i]) for j in range(len(a))))):
            continue
        else:
            return "No"
    return "Yes"

def process(a, b):
    dict_of_a = {}

    for i in range(len(a)):
        if (a[i] not in b):
            return "No"
        if (a[i] in dict_of_a):
            if (i % 2):
                dict_of_a[a[i]][0] = dict_of_a[a[i]][0] + 1
            else:
                dict_of_a[a[i]][1] = dict_of_a[a[i]][1] + 1
        else:
            if i % 2:
                dict_of_a[a[i]] = [1, 0]
            else:
                dict_of_a[a[i]] = [0, 1]
    print dict_of_a
    for i in range(len(b)):
        if (b[i] not in dict_of_a):
            return "No"
        if (b[i] in dict_of_a):
            if (i % 2):
                dict_of_a[b[i]][0] = dict_of_a[b[i]][0] - 1
            else:
                dict_of_a[b[i]][1] = dict_of_a[b[i]][1] - 1
    print dict_of_a
    for k, v in dict_of_a.items():
        if all(v[i] == 0 for i in range(len(v))):
            continue
        else:
            return "No"
    return "Yes"

def twins(a, b):

    result = []
    for i in range(len(a)):
        result.append(process(a[i], b[i]))
    return result

print twins(["cdab", "dcba"], ["abcd", "abcd"])
print twins(["abbc", "abbdd"], ["abbc", "ddbba"])