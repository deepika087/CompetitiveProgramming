__author__ = 'deepika'

class Solution:

    def matchCode(self, code, shopping, startPtr):

        index = 0
        pattern_potential = False
        for i in range(startPtr, len(shopping)):
            if pattern_potential and index >= len(code):
                return True, i

            if pattern_potential and shopping[i] != code[index] and code[index] != 'anything':
                index = 0
                pattern_potential = False

            if shopping[i] == code[index] or code[index] == 'anything' :
                index += 1
                pattern_potential = True

        return (pattern_potential and index >= len(code), i)

    def match(self, codeList, shoppingList):

        res = True
        startPtr = 0
        for code in codeList:
            result, startPtr = self.matchCode(code, shoppingList, startPtr)
            res &= result
            if startPtr >= len(shoppingList) or not res:
                return False
        return True

s=Solution()
print(s.match(["banana", 'anything', 'banana'], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
print(s.match(["banana", 'anything', 'apple'], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
print(s.match([ [ 'apple', 'apple' ], ["banana", 'anything', 'banana'] ],
                  ['banana', 'orange', 'banana','apple', 'apple' ]))
print(s.match([ ["banana", 'anything', 'banana'], [ 'apple', 'apple' ] ],
                  ['banana', 'orange', 'banana','apple', 'apple' ]))
print(s.match([ [ 'apple', 'apple' ], [ 'apple', 'apple', "banana"] ],
                  ['apple', 'apple', 'apple', 'apple', 'banana' ]))
print(s.match([ [ 'apple', 'apple' ], [ 'apple', 'apple', "banana"] ],
                  ['apple', 'apple', 'apple', 'banana' ]))