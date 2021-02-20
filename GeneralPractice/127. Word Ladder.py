__author__ = 'deepika'

"""
Runtime: 884 ms, faster than 16.04% of Python online submissions for Word Ladder.
Memory Usage: 13.8 MB, less than 82.39% of Python online submissions for Word Ladder.

optimizations:

1.) wordList = set(wordList)
2.) isEnd feature to pre-emptively end.
3.) remove from wordlist once that word has been processed.
4.) Switch the positions of clause, newWord not in visited and newWord in wordList
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or len(wordList) == 0:
            return 0

        wordList = set(wordList)

        queue = [beginWord]

        visited = set()
        level = 1
        while (len(queue) > 0):
            nextLevel = []

            while len(queue) > 0:
                popped = queue.pop(0)

                if popped == endWord:
                    return level

                neighbours, isEnd = self.getNeighbours(popped, visited, wordList, endWord)
                if isEnd: #Found
                    return level + 1

                if len(neighbours) > 0:
                    nextLevel += neighbours

                visited.add(popped)

            queue = nextLevel
            level += 1

        return 0

    def getNeighbours(self, startWord, visited, wordList, endWord):
        #print(dis)
        char_set = "qwertyuiopasdfghjklzxcvbnm"
        neigh  = []

        for i in range(len(startWord)):
            for j in char_set:
                if j != startWord[i]:
                    newWord = startWord[0:i] + j + startWord[i + 1: ]
                    if newWord == endWord:
                        return [], True
                    if (newWord not in visited and newWord in wordList):
                        neigh.append(newWord)
                        wordList.remove(newWord)

        return neigh, False



s=Solution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength("a", "c", ["a", "b", "c"]))
print(s.ladderLength("hot", "dog", ["hot", "dog"]))
print(s.ladderLength("qa",
"sq",
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))