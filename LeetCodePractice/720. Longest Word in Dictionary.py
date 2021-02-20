
__author__ = 'deepika'


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = []
        for _word in sorted(words, key=lambda x: len(x), reverse=True):
            if len(result) > 0 and len(_word) < len(result[0]):
                continue
            if self.check(_word, words):
                result.append(_word)

        if len(result) > 1:
            return sorted(result)[0]
        return result[0]


    def check(self, word, words):
        if len(word) == 0 and word in words:
            return True
        elif len(word) == 0 and word not in words:
            return False
        if len(word) == 1 and word in words:
            return True
        elif len(word) == 1 and word not in words:
            return False
        return word[:-1] in words and self.check(word[:-1], words)

s=Solution()

print s.longestWord(["w","wo","wor","worl", "world"])
print s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])