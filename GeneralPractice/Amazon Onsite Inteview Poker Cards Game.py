__author__ = 'deepika'


"""
As we all know that poker cards have four suites: Spades, Hearts, Clubs and Diamonds with figures from 1 to 13.
Now you are given a set of poker cards, you can pick any one card as the first card. And except for the first card, you can only pick the card that has the same suit or figure with the previous one.
Return the max number of cards you can.
For example: [(H, 3), (H, 4), (S, 4), (D, 5), (D, 1)], it returns 3 as follows: (H,3)-->(H,4)-->(S,4)

Apprach: DFS with backtracking
Time Complexity: Exponential 2^n
"""


class Solution:

    def findMaxConnectedComponents(self, cards):

        maxComponent = -float('inf')

        for card in cards: #For each card Do DFS
            path = [card]
            potentialLength = [0]

            visited = set()
            visited.add(card)

            self.startDFS(card, visited, path, potentialLength, cards)
            maxComponent = max(maxComponent, potentialLength[0])

        return maxComponent

    #For each card explore all possibilites. For ex: A -> b -> C also explore A -> C -> B
    # Hence, we need to use backtracking here
    def startDFS(self, card, visited, path, potentialLength, cards):

        neighbours = self.getNeighbours(card, visited, cards)

        if len(neighbours) == 0:
            potentialLength[0] = max(potentialLength[0], len(path))
            return

        for neigh in neighbours:
            visited.add(neigh)
            path.append(neigh)
            self.startDFS(neigh, visited, path, potentialLength, cards)
            visited.remove(neigh)
            path.pop()

    def getNeighbours(self, start, visited, cards):
        neighbours = []

        for card in cards:
            if start != card and card not in visited:
                if card[0] == start[0] or card[1] == start[1]:
                    neighbours.append(card)
        return neighbours

s=Solution()
print(s.findMaxConnectedComponents([("H", 3), ("H", 4), ("S", 4), ("D", 5), ("D", 1) ]))
print(s.findMaxConnectedComponents( [ ("H", 2),("H", 3), ("H", 4), ("S", 4), ("D", 5), ("D", 1) ] ))
print(s.findMaxConnectedComponents( [ ("H",2),("H", 3), ("H", 4), ("S", 2), ("D", 3), ("C", 4), ("C", 7) ] ))