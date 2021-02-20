__author__ = 'deepika'


class Solution(object):
    def traverse(self, safestates, target):

        if (target not in safestates or len(safestates) == 0):
            return -1

        length = len(safestates[0])

        init = ['0' for i in range(length)]
        dis = 0
        stack = [ (init, dis)]

        visited = []

        while (len(stack) > 0):
            popped = stack.pop(-1)
            print("Popped: ", popped[0])

            if (popped[0] in visited):
                continue
            else:
                visited.append(popped[0])

            if (''.join(popped[0]) == target):
                return popped[1]

            dis = dis + 1
            neigh = self.getNeigh(popped[0], safestates, length, visited, dis)

            if len(neigh) > 0:
                stack += neigh
        return -1


    def getNeigh(self, currState, safestates, length, visited, effectiveDistance):

        neigh = []
        for i in range(0, length):
            newState = currState[0:i] + ['1'] + currState[i + 1:]
            if ''.join(newState) in safestates and newState not in visited: #one of the acceptable states
                neigh.append( (newState, effectiveDistance ))

        return neigh

s=Solution()
print("Test case 1: ")
print(s.traverse(["001", "010", "100", "011", "111", "101"], "111"))
print("Test case 2: ")
print(s.traverse(["0010", "0100", "1000", "0110","0111", "1111", "0101"], "1111"))