__author__ = 'deepika'


class Locker:

    def __init__(self, id, capacity, Level):
        self.id = id
        self.capacity = capacity
        self.level = Level
        self.occupied = False
        #Other meta Data goes here. For instance passcode, LastAccessedTime.
        # Functions Like: resetPassCode(), makeAvailable(), generatePassCode() etc

    def __repr__(self):
        return "[" + str(self.id) + ", " + str(self.capacity) + ", " + str(self.level) + "]"

    def markoccupied(self):
        self.occupied = True

class System:

    def __init__(self):
        self.lockers = []

    def addLocker(self, l):
        self.lockers.append(l)

    def findBestLocker(self, requiredCapacity):

        if len(self.lockers) == 0:
            return "No Lockers available"

        unOccupiedLockers = filter(lambda x: x.occupied == False, self.lockers)

        unOccupiedLockers = sorted(unOccupiedLockers, key=lambda x: (x.capacity, x.level))

        if len(unOccupiedLockers) == 0 or requiredCapacity > unOccupiedLockers[len(unOccupiedLockers) - 1].capacity:
            return None

        left = 0
        right = len(unOccupiedLockers) - 1

        while left <= right:
            mid = (right + left)/2

            if unOccupiedLockers[mid].capacity == requiredCapacity:
                unOccupiedLockers[mid].markoccupied()
                return "Locker Provided: ", unOccupiedLockers[mid]

            if unOccupiedLockers[mid].capacity <= requiredCapacity <= unOccupiedLockers[mid+1].capacity:
                if unOccupiedLockers[mid].capacity - requiredCapacity >= 0: # Image Locker as 2, 4, 5 and you are looking for 3. Even if you ocrrectly identify range (2, 4) that won't be enough
                    unOccupiedLockers[mid].markoccupied()
                    return "Locker Provided: ", unOccupiedLockers[mid]
                else:
                    unOccupiedLockers[mid+1].markoccupied()
                    return "Locker Provided: ", unOccupiedLockers[mid + 1]

            elif unOccupiedLockers[mid].capacity > requiredCapacity:
                right = mid - 1
            else:
                left = mid + 1

        return "No Lockers available"


l1 = Locker(1, 1, 1)
l2 = Locker(2, 7, 2)
l3 = Locker(3, 10, 2)
l4 = Locker(4, 5, 2)
l5 = Locker(5, 2, 1)
l6 = Locker(6, 15, 3)
l7 = Locker(7, 1, 1)

s=System()
s.addLocker(l1)
s.addLocker(l2)
s.addLocker(l3)
s.addLocker(l4)
s.addLocker(l5)
s.addLocker(l6)
s.addLocker(l7)

print(s.findBestLocker(3))
print(s.findBestLocker(12))
print(s.findBestLocker(9))
print(s.findBestLocker(7))






