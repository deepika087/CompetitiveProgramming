__author__ = 'deepika'

"""
Runtime: 48 ms, faster than 59.32% of Python online submissions for Maximum Score Words Formed by Letters.
Memory Usage: 13.6 MB, less than 10.17% of Python online submissions for Maximum Score Words Formed by Letters.


This is amazon problem. slightly different as there is no score now.
Given a list of words and list of letters. Words can be formed by using letters given and each letter can only be used once.Find maximum no of letters that can be used from the given list to form the words from the word list.

For example
(1) words=['dog','og','cat']
letters=['o','g','d']
Output: dog
Explanation: Using the given letters we can form [dog] and [og] but output the longer word

(2) words=[dog,do,go]
letters=[d,o,g,o]
Output: do,go
Explanation: Here we can either form [dog] or [do,go] but pick the one which requires more leters.
"""
import collections

class Solution(object):

    maxProfit = -float('inf')
    maxCharCount = -float('inf')

    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        words = [collections.Counter(w) for w in words]
        letters = collections.Counter(letters)

        #print(words)
        #print(letters)
        profit_so_far = 0
        self.startRecursion(0, words, letters, score, profit_so_far)
        return self.maxProfit

    def startRecursion(self, i, words, letters, score, profit_so_far):

        if i == len(words):
            self.maxProfit = max(self.maxProfit, profit_so_far)
            #print(self.maxProfit)
            return self.maxProfit

        if all( letters[w[0]] >= words[i][w[0]] for w in words[i].items()):

            temp_profit = 0
            for w in words[i].items():
                letters[w[0]] -= words[i][w[0]]
                temp_profit += words[i][w[0]] * score[ord(w[0]) - ord('a')]
            self.startRecursion(i + 1, words, letters, score, profit_so_far + temp_profit)

            for w in words[i].items():
                letters[w[0]] += words[i][w[0]]

        self.startRecursion(i + 1, words, letters, score, profit_so_far)

    print


"""
s1=Solution()
print(s1.maxScoreWords(words = ["dog","cat","dad","good"],
                letters = ["a","a","c","d","d","d","g","o","o"],
                score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))

s2=Solution()
print(s2.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))
"""

s3=Solution()
print(s3.maxWords(words = ["dog","cat","dad","good"],
                letters = ["a","a","c","d","d","d","g","o","o"]))

s4=Solution()
print(s4.maxWords(words=['dog','og','cat'], letters=['o','g','d']))

s5=Solution()
print(s5.maxWords(words=['dog','do','go'], letters=['d', 'o','g','o']))