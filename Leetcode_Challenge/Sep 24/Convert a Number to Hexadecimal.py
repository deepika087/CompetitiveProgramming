
"""
The logic is not correct here.
"""
def toHex(num):
    result = ''
    while(num > 0):
        if (num >= 16):
            remainder = num % 16;
            quotient = num/16;
            result = result + "012345689ABCDEF"[quotient]
            num = remainder
        else:
            result = result + "012345689ABCDEF"[num-1]
            num = 0; #to exit the loop
        print "Updating result to : ", result
    return result

if __name__=="__main__":
    num = 48
    print toHex(num)