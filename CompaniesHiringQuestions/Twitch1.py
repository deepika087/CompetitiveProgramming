__author__ = 'deepika'


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
The most stupidiest question ever.
It was something like replace spaces and dashes and reformat phone numbers.
"""
def solution(S):

    SNew = S.replace('-', '')
    SNew = SNew.replace(' ', '')
    #print(S)

    i = 0
    result = []
    while i < len(SNew):
        result.append(SNew[i:i+3])
        i += 3

    if len(result[len(result) - 1]) == 3 or len(result[len(result) - 1]) == 2 : # If last block is of length 3
        return '-'.join(result)
    else:
        # If last block has less than 3 characters in it
        digitcount = 0
        dashcount = 0
        for i in range(len(S)-1, -1, -1):
            if digitcount == 4 and dashcount == 0:
                return '-'.join(result)

            if digitcount == 4 and dashcount > 0:
                break

            if ord(S[i]) >= ord('0')  and ord(S[i]) <= ord('9'):
                digitcount += 1

            if S[i] == '-':
                dashcount += 1

        if dashcount > 0:
            lastBlock = result.pop()
            secondLastBlock = result.pop()


            result = '-'.join(result)
            if len(result) > 0:
                result += '-'
            for i in range(len(secondLastBlock) - 1):
                result += secondLastBlock[i]
            result += '-' + secondLastBlock[len(secondLastBlock)-1]

            for i in range(len(lastBlock)):
                result += lastBlock[i]

            return result
    return '-'.join(result)

print(solution("0 - 22 1985--324")) #special case 022-198-53-24
print(solution("00-44    12-7384-   939"))
print(solution("00-44    48 5555 8361"))
print(solution("00-44    48 5555   - --- -   8361"))
print(solution("00-44    48 5555   - --- -   83-61"))
print(solution("00-44    48 5555 8-361"))
print(solution("00-44    48 555 8-361"))

print(solution("00-44"))
print(solution("9"))
print(solution("00-44     1   2-7384  939"))
print(solution("00-44     1   2-738-4  939"))

