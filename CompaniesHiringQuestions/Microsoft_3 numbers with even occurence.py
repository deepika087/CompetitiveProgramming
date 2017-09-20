"""
Given an array of integers,there are 3 numbers which occur even number of times.
Find those numbers and print them in the order they first appear in the array.
"""


def displayNumbers(numbers):

    odd = 0
    even = 0

    for i in numbers:
        if (1<<i & odd) > 0: #Actually an even occurence
            #Unset from even number
            even |= 1<<i
        else: #Odd occurence
            odd |= 1<<i
            #Unset from even number

if __name__=="__main__":
    print displayNumbers([2,2,2,2,1,3,3,4,4,6,8])