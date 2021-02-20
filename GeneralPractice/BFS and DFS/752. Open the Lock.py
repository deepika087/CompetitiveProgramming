__author__ = 'deepika'

"""
Runtime: 6016 ms, faster than 5.00% of Python online submissions for Open the Lock.
Memory Usage: 13.7 MB, less than 91.40% of Python online submissions for Open the Lock.
"""

class Solution(object):

    def getNeighbours(self, startPos):

        neighbours = []

        for i in range(len(startPos)):
            nextChar = str( (ord(startPos[i]) - ord('0') + 1) % 10)
            prevChar =  str( ( (ord(startPos[i]) - ord('0') - 1) + 10 ) % 10)

            fwdCombo = startPos[0:i] + nextChar + startPos[i+1:]
            revCombo = startPos[0:i] + prevChar + startPos[i+1:]

            neighbours.append(fwdCombo)
            neighbours.append(revCombo)

        return neighbours

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        start = "0000"
        queue = []
        seen = set()
        queue.append(start)
        seen.add(start)
        level = 0

        if start in deadends:
            return -1

        while len(queue) > 0:
            nextlevel = [] #this is the point I forgot in Facebook interview.

            while len(queue) > 0:
                popped = queue.pop(0)

                if popped == target:
                    return level

                neighbours = self.getNeighbours(popped)

                for neighbour in neighbours:
                    if neighbour in seen:
                        continue
                    if neighbour in deadends:
                        continue
                    if not neighbour in seen:
                        nextlevel.append(neighbour)
                        seen.add(neighbour)

                seen.add(popped)
            queue = nextlevel
            level += 1

        return -1

s=Solution()
print(s.openLock(["0000"], "8888"))
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))
print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))