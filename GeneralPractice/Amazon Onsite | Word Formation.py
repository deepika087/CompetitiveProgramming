__author__ = 'deepika'


class Solution:

    def isPossible(self, string, mapping):

        taken = [False] * len(mapping)
        index = 0
        return self.isPossibleUtil(index, string, taken, mapping)

    def isPossibleUtil(self, index, string, taken, mapping):

        if index >= len(string):
            return True

        result = True
        for i in range(len(mapping)):
            if not taken[i]:
                if mapping[i][0] == string[index] or mapping[i][1] == string[index]:
                    taken[i] = True
                    result &= self.isPossibleUtil(index+1, string, taken, mapping)
                    if result: #At any point if we have found then just return True
                        return True
                    taken[i] = False
        return False #If code is reaching here then for sure not possible.

s=Solution()
print(s.isPossible("A", [ ['A', 'B']]))
print(s.isPossible("BABY", [ ['A', 'B'], ['B', 'A'], ['B', 'X'], ['Y', 'C']]))
print(s.isPossible("BABY", [ ['A', 'B'], ['B', 'A'], ['L', 'E']]))
print(s.isPossible("ABLE", [ ['A', 'B'], ['B', 'A'], ['L', 'E']]))
print(s.isPossible("ABLE", [ ['A', 'B'], ['B', 'A'], ['L', 'E'], ['E', 'O']]))