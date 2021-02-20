

def func1(listInput):
    listInput[2] = -1
    return sorted(listInput)
    return listInput

if __name__ == "__main__":
    list1 = []
    list1.append(1)

    print "List1 : ", list1

    list2 = [3, 0, 19, 1, 9]
    list3 = [4, 5, 6]

    print "list before: ", list2
    print "Calling function"
    print "list after: ", func1(list2)
    print "list2 as it is : ", list2

    #func1(list)
