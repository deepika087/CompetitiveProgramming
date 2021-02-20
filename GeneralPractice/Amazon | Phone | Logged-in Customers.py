__author__ = 'deepika'


"""
A new line "<customerId>,<timestamp>" is added to a log file and saved on a disk, for example
Write a method to find customers who logged-in on Amazon.com "X" times (2, 14 or any other number of times) for the past 24 hours.

Intution: maintain two hashmaps userTocounts and countToUser.
Array is a queue contains all tuples so far. every time we append a new log we compare if we see if there are eligible records
for pruning.

Everytime you prune. make sure userToCounts is decremented by one Also for countToUser make sure you not only remove this user
from the prev count but also add it to the new count which is actually old count - 1

similar logic works for addition.

Assumption: Logs occur in the increasing order of time.
Time complexity:
    findUserWithCount - O(1)
    Prune - O(1) on average
"""
class Solution:

    def __init__(self):
        self.array = []
        self.countToUserMapping = dict()
        self.userToCountMapping = dict()

    def log(self, input):

        user, ts = input.split(",")
        ts = int(ts)

        #Prune the list
        while self.array and abs(self.array[0][1] - ts) >= 24:
            popped = self.array.pop(0)
            countTofix = self.userToCountMapping.get( popped[0] )

            if countTofix == 1:
                del self.userToCountMapping[popped[0]]
            else:
                self.userToCountMapping[popped[0]] -= 1

                if countTofix - 1 not in self.countToUserMapping:
                    self.countToUserMapping[countTofix - 1] = []
                self.countToUserMapping[countTofix - 1].append(popped[0])

            self.countToUserMapping[countTofix].remove(popped[0])

        self.array.append( [user, ts] )
        if user in self.userToCountMapping:
            oldCount = self.userToCountMapping[user]
            self.countToUserMapping[oldCount].remove( user )

            self.userToCountMapping[user] += 1
            if oldCount + 1 not in self.countToUserMapping:
                self.countToUserMapping[oldCount + 1] = []
            self.countToUserMapping[oldCount + 1].append( user )

        else:
            self.userToCountMapping[user] = 1
            if 1 not in self.countToUserMapping:
                self.countToUserMapping[1] = []
            self.countToUserMapping[1].append( user )


    def findUserWithCount(self, x):

        return self.countToUserMapping.get(x, [])


s=Solution()
s.log("a, 1")
s.log("b, 1")
print(s.findUserWithCount(1))
s.log("a, 2")
print(s.findUserWithCount(2)) # a should not show here
s.log("c, 3")
print(s.findUserWithCount(1)) # b anc c both should show
print(s.findUserWithCount(3))
s.log("c, 4")
s.log("c, 5")
print(s.findUserWithCount(1)) # only b should print
print(s.findUserWithCount(3))
s.log("c, 6")
s.log("d, 25")
print(s.findUserWithCount(1)) # now a should come back. bcz a at ts = 1 should have been deleted by now.


