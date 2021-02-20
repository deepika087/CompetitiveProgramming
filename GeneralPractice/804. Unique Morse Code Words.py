__author__ = 'deepika'



class Solution(object):

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        results = {}
        for word in words:
            output = ""
            for i in range(len(word)):
                output += codes[ord(word[i]) - ord('a')]
            if output in results:
                results[output] += 1
            else:
                results[output] = 1
        return len(results.keys())

s=Solution()
print s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])

