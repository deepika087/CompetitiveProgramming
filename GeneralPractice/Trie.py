__author__ = 'deepika'


class TrieNode:
    def __init__(self):
        self.hashMap = dict()
        self.isEndOfWord = False

    def __repr__(self):
        return str(self.hashMap)

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):

        root = self.trie

        for i in range(len(word)):
            character = word[i]
            if character not in root.hashMap:
                root.hashMap[word[i]] = TrieNode()
            root = root.hashMap[word[i]]
        root.isEndOfWord = True

    def displayAll(self):
         root = self.trie
         path = ""
         self.displayUtil(root, path)

    def displayUtil(self, startPoint, path):
        if startPoint == None:
            return

        if startPoint.isEndOfWord:
            print("path so far: ", path)

        for (k, v) in startPoint.hashMap.items():
            self.displayUtil(startPoint.hashMap[k], path + k)


    def displayWithPrefix(self, prefix):
        root = self.trie

        for i in range(len(prefix)):
            if prefix[i] in root.hashMap:
                root = root.hashMap[prefix[i]]
            else:
                break

        self.displayUtil(root, prefix)

trie = Trie()
trie.insert("deepika")
trie.insert("deepikaananad")
trie.insert("deepdkjhkjdhkjda")
trie.insert("d")
trie.insert("anand")
trie.insert("x")
trie.insert("rihana")
trie.insert("raj")
trie.insert("rananaji")
trie.insert("rakesh")
trie.displayAll()
print("Display with Prefix")
trie.displayWithPrefix("d")
#print(trie.trie)
#trie.displayWithPrefix("r")



