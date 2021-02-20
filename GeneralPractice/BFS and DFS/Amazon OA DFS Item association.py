t__author__ = 'deepika'


"""
Q1. Given a list of item association relationships, write an algorithm that outputs the largest item association group. If two groups have the same number of items then select the group which contains the item that appears first in lexicographic order.

Input :
[[Item1, Item2], [Item3, Item4], [Item4, Item5]]

Output :
[Item3, Item4, Item5]
"""

class Solution(object):

    def dataRepresentation(self, itemAssociation):

        uniqueItems = set()
        items = dict()

        for association in itemAssociation:
            #print(association)
            uniqueItems.add(association[0])
            if association[0] not in items:
                items[association[0]] = [association[1]]
            else:
                items[association[0]].append(association[1])

            if association[1] not in items:
                items[association[1]] = [association[0]]
            else:
                items[association[1]].append(association[0])

        return items, uniqueItems

    def largestItemAssociation(self, itemAssociation):

        results = []

        items, nodes = self.dataRepresentation(itemAssociation)
        visited = set()

        for node in nodes:
            if node in visited:
                continue
            else:
                result = []
                self.startDFS(node, items, visited, result)
                if len(results) == 0:
                    results.append(sorted(result))
                elif len(result) > len(results[0]): #remove previous results and just overwrite
                    results = sorted(result)
                elif len(result) == len(results[0]): # Got a candidate
                    results.append(sorted(result))
        return sorted(results)

    def startDFS(self, node, items, visited, result):

        visited.add(node)

        for neigbour in items[node]:
            if neigbour in visited:
                continue
            self.startDFS(neigbour, items, visited, result)
        result.append(node)

s=Solution()
print(s.largestItemAssociation([['A', 'B'], ['C', 'D'], ['D', 'E']]))
print(s.largestItemAssociation([['A', 'B'], ['C', 'D'], ['F', 'E']]))
print(s.largestItemAssociation([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]))
print(s.largestItemAssociation([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]))
print(s.largestItemAssociation([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C'], ['F', 'E'], ['X', 'G'],['X', 'N'], ['G', 'K'], ['K', 'L'], ['L', 'M']]))

