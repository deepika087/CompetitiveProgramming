__author__ = 'deepika'



class Cat:

    def __init__(self, catID, ht, wgt):
        self.ID = catID
        self.ht = ht
        self.wt = wgt

    def __str__(self):
        return "[ " + str(self.ID) + " , " + str(self.ht) + " , " + str(self.wt)  + " ]"

    def __repr__(self):
        return self.__str__()


class Solution:

    def __init__(self, cats):

        self.htDict = dict()
        self.wtDict = dict()
        self.cats = cats


    def assignDictValues(self, htconstraint, wtconstraint):

        self.htDict['<'] = lambda x: x.ht < htconstraint
        self.htDict['>'] = lambda x: x.ht > htconstraint

        self.wtDict['<'] = lambda x: x.wt < wtconstraint
        self.wtDict['>'] = lambda x: x.wt > wtconstraint

    def filterVaues(self, comparatorht, valueht, cwt, valuewt):
        self.assignDictValues(valueht, valuewt)

        print("Cats with ", comparatorht, " with height ", valueht)
        print(list(filter(self.htDict[comparatorht], self.cats)))

        print("Cats with ", cwt, " with height ", valuewt)
        print(list(filter(self.wtDict[cwt], self.cats)))

c1 = Cat("c1", 10, 5)
c2 = Cat("c2", 5, 10)
c3 = Cat("c3", 6, 9)
c4 = Cat("c4", 1, 1)
c5 = Cat("c5", 8, 12)

s=Solution([c1, c2, c3, c4, c5])
s.filterVaues('<', 10, '>', 5)





