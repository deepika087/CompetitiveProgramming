__author__ = 'deepika'
import copy

dictionary = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
}

def dfs(string, result, results):

    if len(string) == 0:
        results.append(result)
        return result

    First, remaining = string[0], string[1:]
    Letters = dictionary[First]
    for _l in Letters:
        dfs(remaining, result + _l, results)



def combinations(number):
    results = []
    dfs(number, "", results)

    print results


class Solution(object):
    def __init__(self):
        self.mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, input):
        if len(input) == 0:
            return
        startIndex  = 0
        offset = 0
        self.constructRecurse(input, startIndex, offset, "")

    def constructRecurse(self, input, index, offset, builder):
        #print "Called with index = ", index , " offset = ", offset, " builder ", builder
        if index == len(input) - 1:
            #print "Exiting with ", builder + self.getChar(input[index], offset)
            print builder + self.getChar(input[index], offset)
            return

        self.constructRecurse(input, index + 1, 0, builder + self.getChar(input[index], offset))

        #print "Comparinrg: ", input[index + 1] , " ", input[index], "with offset = ", offset, " builder ", builder
        if input[index + 1] == input[index]:
            #print "with index = ", index, " ", builder, "  with offset = ", offset
            self.constructRecurse(input, index + 1, offset + 1, builder)

    def getChar(self, num, offset):
        return self.mapping[num][offset % len(self.mapping[num])]

s=Solution()
input="223"
print "====Facebook Expectation===="
print s.letterCombinations(input)

print "====Normal DFS==="
combinations(input)
