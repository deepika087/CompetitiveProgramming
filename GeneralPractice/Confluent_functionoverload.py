__author__ = 'deepika'

"""
first of all design a trie. For each function maintain two lists - one for function ending at this nodes which have isvar
equal to True and one for functions ending at this node and isvar is false.

Now, when you traverse the new argument list say I, I, I. For any argument which is not the last arg for instance
the first two I in this case, check if the current node has any isVarTrue list.
    - Now check if all the successor arg[i:] are same as the current Node we are at. If yes, this means our
    isVar condition is satisfied.
If it is the last argument, then check for True list + false list.
"""

class Node:
    def __init__(self):
        self.hashMap = dict()
        self.isVarTrue = []
        self.isVarFalse = []

    def __repr__(self):
        return " HashMap : " + str(self.hashMap) + '\n' + " VarTrue: " + str(self.isVarTrue) + '\n' + "VarFalse: " + str(self.isVarFalse)

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, funcName, arguments, isVariable):
        start = self.root

        for arg in arguments:
            if arg not in start.hashMap:
                start.hashMap[arg] = Node()
            start = start.hashMap[arg]

        if isVariable:
            start.isVarTrue.append(funcName)
        else:
            start.isVarFalse.append(funcName)

    def allSame(self, listInput, arg):

        i = 0
        while i < len(listInput):
            if listInput[i] != arg:
                return False
            i+=1
        return True

    def match(self, arguments):

        start = self.root
        result = []

        for i in range(len(arguments)):
            arg = arguments[i]
            if not arg in start.hashMap:
                return result
            else:
                if i != len(arguments)-1 and len(start.hashMap[arg].isVarTrue) > 0:
                    if self.allSame(arguments[i:], arg):
                        result.append(start.hashMap[arg].isVarTrue)
                if i == len(arguments) - 1:
                    if len(start.hashMap[arg].isVarTrue) > 0:
                        result.append(start.hashMap[arg].isVarTrue)
                    if len(start.hashMap[arg].isVarFalse) > 0:
                        result.append(start.hashMap[arg].isVarFalse)
                start = start.hashMap[arg]
        return result

t=Trie()
t.insert("FuncA", ["String", "Integer", "Integer"], False)
t.insert("FuncB", ["String", "Integer"], True)
t.insert("FuncC", ["Integer"], True)
t.insert("FuncD", ["Integer", "Integer"], True)
t.insert("FuncE", ["Integer", "Integer", "Integer"], False)
t.insert("FuncF", ["String"], False)
t.insert("FuncG", ["Integer"], False)
#print(t.root)

print("Print match")
print(t.match(["String"])) #[FuncF]
print(t.match(["Integer"])) #[FuncC, FuncG]
print(t.match(["Integer", "Integer", "Integer", "Integer"])) #[FuncC, FuncD]
print(t.match(["Integer", "Integer", "Integer"])) #[FuncC, FuncD, FuncE]
print(t.match(["String", "Integer", "Integer", "Integer"])) #FuncB
print(t.match(["String", "Integer", "Integer"])) #FuncA,FuncB