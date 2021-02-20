__author__ = 'deepika'

"""
Succesful part was that if one combo is possible then return.

Runtime: 28 ms, faster than 68.54% of Python online submissions for Word Break.
Memory Usage: 14 MB, less than 10.87% of Python online submissions for Word Break.

Runtime: 28 ms, faster than 81.94% of Python online submissions for Word Break II.
Memory Usage: 13.6 MB, less than 98.91% of Python online submissions for Word Break II.

139. Word Break

"""

class Solution:

    def wordBreakGeneric(self, words):

        for i in range(len(words)):

            wordDict = []
            wordDict += words[0:i]
            wordDict += words[i+1:]
            result = self.wordBreak(words[i], wordDict)
            print(words[i], result)

    def wordBreak(self, string, words):
        return self.startbfs(string, words)

    def startbfs(self, string, words):

        letters = set(string)
        complete_strng = set(''.join(words))
        if not all(char in complete_strng for char in letters):
            return []

        result = []
        queue = [ [string[0], 0] ]

        #Visited can be removed if you want to find multiple possibilties. For just a answer, visited can be used
        visited = set()
        visited.add(0)

        while queue:

            popped, index = queue.pop()

            if index >= len(string):
                popped.pop(-1)
                result.append(" ".join(popped[::-1]))
                continue

            for word in words:
                if word.startswith(string[index]) and index + len(word) <= len(string) and string[index:index + len(word)] == word:
                    groups = [word]
                    groups+=popped
                    queue.append( [ groups, index + len(word)])

        return result




s=Solution()
print(s.wordBreakGeneric(["amazon", "ama", "zon", "leetcoderocks", "leet", "code", "rocks", "leetcode"]))
print(s.wordBreak("abcdefghijklmnopqrstuvwxyz", ["abc", "defg", "def", "g", "gh","ijklmno", "ghijklmno", "pqrstuvwxyz", "pqrst", "uvwxyz"]))
print(s.wordBreak("pineapplepenapple",  ["apple", "pen", "applepen", "pine", "pineapple"]))
print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(s.wordBreak("aaaaaaaa",
["aaaa","aa","a"]))
