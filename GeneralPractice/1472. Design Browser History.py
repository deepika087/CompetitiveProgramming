__author__ = 'deepika'

"""
Runtime: 224 ms, faster than 57.99% of Python online submissions for Design Browser History.
Memory Usage: 16.4 MB, less than 24.54% of Python online submissions for Design Browser History.
"""

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.sites = []
        self.cur = 0
        self.sites.append(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.sites[self.cur + 1:] = ""
        self.sites.insert(self.cur + 1, url)
        self.cur += 1


    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cur - steps >= 0:
            self.cur -= steps
        else:
            self.cur = 0

        return self.sites[self.cur]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.cur + steps <= len(self.sites) - 1:
            self.cur += steps
        else:
            self.cur = len(self.sites) - 1
        return self.sites[self.cur]





# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin.com")
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))