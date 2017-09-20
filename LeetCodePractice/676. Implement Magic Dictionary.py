__author__ = 'deepika'
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.EntireSet = []



    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for x in dict:
            self.EntireSet.append(x)
        print self.EntireSet



    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        



# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary()
obj.buildDict(["hello", "leetcode"])
# param_2 = obj.search(word)