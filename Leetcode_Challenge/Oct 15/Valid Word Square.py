"""
422. Valid Word Square

33 / 33 test cases passed.
Status: Accepted
Runtime: 129 ms
"""
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        k_dummy = max(len(i) for i in words)
        k = max(len(words), k_dummy)

        for i in range(k):
            row = words[i]
            col = []
            for j in range(len(words)):
                #print " At j = ", j, "len = ", len(words[j]), " i = ", i
                if (i < len(words[j])):
                    #print " Re"
                    col.append(words[j][i])
            col = "".join(col)
            #print " Comparing row = ", row, " and col = ", col
            if (row == col):
                continue
            else:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print sol.validWordSquare([
          "ball",
          "area",
          "read",
          "lady"
        ]);

    print sol.validWordSquare([
          "abcd",
          "bnrt",
          "crm",
          "dt"
        ]);

    print sol.validWordSquare([
          "abcd",
          "bnrt",
          "crmy",
          "dtye"
        ]);