__author__ = 'deepika'


"""
Runtime: 144 ms, faster than 40.16% of Python online submissions for Insert Delete GetRandom O(1).
Memory Usage: 17.9 MB, less than 97.46% of Python online submissions for Insert Delete GetRandom O(1).

Another Idea: How about just the map. But then how will I delete given the index.
"""
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.setData = set()
        self.data = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.setData:
            return False
        self.setData.add(val)
        self.data.append(val)
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.setData:
            return False

        self.setData.remove(val)
        self.data.remove(val)
        return True



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        r = random.randint(0, len(self.data)-1)
        return self.data[r]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(5)
param_2 = obj.remove(10)
param_3 = obj.getRandom()
print(param_3)