__author__ = 'deepika'

import queue as Q

class Skill(object):
    def __init__(self, priority, timestamp, description):
        self.priority = priority
        self.timestamp = timestamp
        self.name = description

    def __cmp__(self, other):
        if (self.priority > other.priority):
            return -1
        elif(self.priority < other.priority):
            return 1
        else: #If equal
            if (self.timestamp < other.timestamp):
                return -1
            elif (self.timestamp > other.timestamp):
                return 1
            return 0

    def __repr__(self):
        #return "[" + str(self.priority) + " " + str(self.timestamp) + " " + str(self.name) + "]"
        return self.name

if __name__ == "__main__":
    n = int(raw_input(''))
    q = Q.PriorityQueue()
    timestamp=0
    for _ in range(n):
        inputLine = raw_input('')
        inputLine = inputLine.split()
        if (inputLine[0] == 'store'):
            timestamp=timestamp + 1
            q.put(Skill(int(inputLine[2]), timestamp, inputLine[1]))
        else:
            print q.get()
