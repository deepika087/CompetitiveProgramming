__author__ = 'deepika'

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or len(wordList) == 0:
            return []

        wordList = set(wordList)

        queue = [ [beginWord ] ]
        result = []
        visited = set()
        level = 1
        while (len(queue) > 0):
            nextLevel = []

            while len(queue) > 0:
                path = queue.pop(0)
                popped = path[0]

                if popped == endWord:
                    if len(result) == 0 or len(result[0]) == level:
                        result.append(path[::-1])
                    elif level < len(result[0]):
                        result = [ path[::-1] ]

                neighbours = self.getNeighbours(popped, visited, wordList)

                for neighbour in neighbours:
                    newPath = [neighbour]
                    newPath.extend(path)
                    nextLevel.append( newPath )

                visited.add(popped)

            queue = nextLevel
            level += 1

        return result

    def getNeighbours(self, startWord, visited, wordList):
        #print(dis)
        char_set = "qwertyuiopasdfghjklzxcvbnm"
        neigh  = []

        for i in range(len(startWord)):
            for j in char_set:
                if j != startWord[i]:
                    newWord = startWord[0:i] + j + startWord[i + 1: ]
                    if (newWord not in visited and newWord in wordList):
                        neigh.append(newWord)
                        #wordList.remove(newWord)

        return neigh

s=Solution()
print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] ))