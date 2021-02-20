__author__ = 'deepika'

#631. Design Excel Sum Formula
class Excel(object):

    def __init__(self, H, W):
        """
        :type H: int
        :type W: str
        """
        W = ord(W[0]) - ord('A') + 1
        self.excel = [[ 0 for j in range(W) ] for i in range(H)]
        print self.excel
        #self.H = H
        #self.W = W


    def set(self, r, c, v):
        """
        :type r: int
        :type c: str
        :type v: int
        :rtype: void
        """

        r_prime = r - 1 #offset by 0
        c_prime = ord(c) - ord('A')
        print " Set c: ", c, " so I will set", r_prime, c_prime
        self.excel[r_prime][c_prime] = v

    def get(self, r, c):
        """
        :type r: int
        :type c: str
        :rtype: int
        """
        r_prime = r - 1 #offset by 0
        c_prime = ord(c) - ord('A')
        return self.excel[r_prime][c_prime]

    #Sum(3, "C", ["A1", "A1:B2"]);
    def sum(self, r, c, strs):
        """
        :type r: int
        :type c: str
        :type strs: List[str]
        :rtype: int
        """
        r_prime = r - 1
        c_prime = ord(c) - ord('A')
        sumT = 0
        for str in strs:
          if ':' in str:
            sumT += self.handleRectange(str)
          else:
            r = int(str[1]) - 1
            c = ord(str[0]) - ord('A')
            sumT += self.excel[r][c]
        print "Setting: ", r_prime, " and ", c_prime
        self.excel[r_prime][c_prime] = sumT
        return sumT

    def handleRectange(self, str):
        startRect = str.split(':')[0]
        endRect = str.split(':')[1]
        row_start, col_start = self.handleSlice(startRect)
        row_end, col_end = self.handleSlice(endRect)

        sumT = 0
        for i in range(row_start, row_end + 1):
          for j in range(col_start, col_end + 1):
            sumT += self.excel[i][j]
        return sumT

    def handleSlice(self, str):
        return int(str[1]) - 1, ord(str[0]) - ord('A')








# Your Excel object will be instantiated and called as such:
"""
obj = Excel(3,"C")
obj.set(1, "A", 2)
param_2 = obj.get(1,"A")
print param_2
param_3 = obj.sum(3, "C", ["A1", "A1:B2"])
print param_3
"""

#Input 2
#["Excel","sum","set","get"]
obj = Excel(3,"C")
print " Sum : ", obj.sum(1,"A",["A2"])

print "Dictionary so far:", obj.excel
print obj.get(1,"A")
