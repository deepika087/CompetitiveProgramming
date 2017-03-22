__author__ = 'deepika'


def rollingString(s, operations):
    s=list(s)
    for operation in operations:
        leftPtr = int(operation[0])
        rightPtr = int(operation[2])
        operation = operation[4]

        for i in range(leftPtr, rightPtr + 1):
            if (operation == 'L'):
                if (s[i] == 'a'):
                    s[i] = 'z'
                else:
                    s[i] = chr(ord(s[i]) - 1)
            elif(operation == 'R'):
                if (s[i] == 'z'):
                    s[i] = 'a'
                else:
                    s[i] = chr(ord(s[i]) + 1)
    return ''.join(s)


if __name__ =="__main__":
    print rollingString("abc", ['0 0 L', '2 2 L', '0 2 R'])
    print rollingString("abcqusze", ['0 6 L', '1 4 L', '5 7 R'])