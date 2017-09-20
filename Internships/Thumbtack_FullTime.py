__author__ = 'deepika'
"""
Basically the transactions here are like cache. So we have original value in main database and cached values in transactions.
IF the "begin" block hasn't been seen yet. Then simply execute the instructions on main Table itself.

I have assumed transactions as a List<TransNode> where each TransNode has a dictionary that stored cached value of variables used in that transaction.

For every Begin, add a new Transaction block that is TransNode to stack.
The trickiest event was NUMEQUALTO in Transaction list. For this I have traversed all cached dictionaries. Collected variable whose value matches. However, if that variable has been unset then add that variable to deletedKey set. But again if you see occurence of that varilable in future, this eans this variable was re-entered in system. So, remove that variable from deletedKey and add to matchValue.

Then see if this value occurs in main database, fetch the variable that match value say returned set is "res". In this case print Len(res union matchVAlue difference deletedKey)

Overall, a very good question.
"""


class database(object):
    def __init__(self):
        self.table = dict()

    def getValue(self, _value):
        keys = set()
        for (k, v) in self.table.items():
            if v == _value:
                keys.add(k)
        return keys

    def performFunction(self, input_line):
        if 'SET' in input_line:
            db.table[input_line[1]] = input_line[2]

        elif 'GET' in input_line: #Doesn't matter if begin yet or not. SHow that actual Table data
            print "> " + (str(db.table[input_line[1]]) if input_line[1] in db.table else "NULL")

        elif 'UNSET' in input_line and not beginblock:
            del db.table[input_line[1]]

        elif 'NUMEQUALTO' in input_line: #Will always be executed against the valid database
            return db.getValue(input_line[1])
            #print "> " + str(len(offset))

    def merge(self, tempTrans):
        for k, v in tempTrans.tempTable.items():
            if v == 'DEL':
                del self.table[k]
            else:
                self.table[k] = v

class TransNode(object):
    def __init__(self):
        self.tempTable = dict()

    def __repr__(self):
        return str(self.tempTable)

class Stack:

    def __init__(self):
        self.transactions = []

    def applySentinel(self):
        self.transactions.append(TransNode())

    def add(self, input_line):
        recentTable = self.transactions.pop()
        #print "Most Recent table was: ", recentTable
        if 'SET' in input_line:
            recentTable.tempTable[input_line[1]] = input_line[2]
            self.transactions.append(recentTable)
            return False, None

        elif 'GET' in input_line: #Doesn't matter if begin yet or not. SHow that actual Table data
            self.transactions.append(recentTable)
            return True, (str(recentTable.tempTable[input_line[1]]) if input_line[1] in recentTable.tempTable else "NULL")

        elif 'UNSET' in input_line:
            recentTable.tempTable[input_line[1]] = "DEL"
            self.transactions.append(recentTable)
            return False, None

        elif 'NUMEQUALTO' in input_line: #Will always be executed against the valid database
            self.transactions.append(recentTable)
            matchValue, deletedKey = set(), set()
            for _trans in self.transactions:
                tbl = _trans.tempTable
                for (k, v) in tbl.items():
                    if v == input_line[1]:
                        matchValue.add(k)
                        if k in deletedKey:
                            deletedKey.remove(k) #Re-Add it
                    elif v == 'DEL':
                        deletedKey.add(k)
            return matchValue, deletedKey


            #return True, set(filter(lambda x: x[1] == input_line[1], recentTable.tempTable.items()))

         #Put back

    def undoMostRecentTrans(self):
        if self.transactions:
            self.transactions.pop() #pop from top

    def isTransactionPending(self):
        return len(self.transactions) > 0

    def getValidTransactions(self):
        return self.transactions


if __name__ =="__main__":
    db = database()
    input_line = raw_input()

    beginblock = False
    while input_line:
        print input_line
        input_line = input_line.split(' ')

        if 'END' in input_line:
            break

        if 'ROLLBACK' in input_line and not beginblock or 'COMMIT' in input_line and not beginblock:
                print "> NO TRANSACTION"

        if 'BEGIN' in input_line or beginblock: #Handle Transactions

            if 'BEGIN' in input_line and not beginblock:
                transactions = Stack()
                beginblock = True
                transactions.applySentinel() #Add new transaction
            elif 'BEGIN' in input_line and beginblock:
                transactions.applySentinel()

            elif 'ROLLBACK' in input_line and not beginblock or 'COMMIT' in input_line and not beginblock:
                print "> NO TRANSACTION"
            elif 'ROLLBACK' in input_line and beginblock:
                transactions.undoMostRecentTrans()
                if not transactions.isTransactionPending():
                    beginblock = False

            elif 'COMMIT' in input_line and beginblock:
                _transactions = transactions.getValidTransactions()
                beginblock = False
                for _trans in _transactions:
                    db.merge(_trans)

            else: #Neither of BEGIN, ROLLBACK or COMMIT. Must be a statment

                isPrint, result = transactions.add(input_line)
                if isPrint is not False:
                    if 'GET' in input_line:
                        if result == 'NULL':
                            db.performFunction(input_line)
                        elif result == 'DEL': #It means this must have been deleted
                            print "> NULL"
                        else:
                            print '> ' + result
                    else: #NUMEQUAL TO CASE
                        matchValue, deletedKey = isPrint, result
                        #print matchValue, deletedKey
                        res = db.performFunction(input_line)
                        # Get unset variables from cache
                        #print "Merging: ", res, " ", matchValue
                        res = res.union(matchValue)
                        res = res.difference(deletedKey)
                        print "> " + str(len(res))

        else:
            res = db.performFunction(input_line)
            if "NUMEQUALTO" in input_line:
                print "> " + str(len(res))


        #print db.table
        input_line = raw_input()

