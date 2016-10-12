"""
5. Longest Palindromic Substring
Using DP, but works for small inputs. Use Manchester's Algo for long inputs
"""

def longestPalindromeGFG(s):
    #print " Received ", s
    n = len(s)
    table = [ [ 0 for _ in range(n)] for _ in range(n) ]
    start = 0;
    maxLen = 1
    for i in range(n-1):
        table[i][i] = True
        if s[i] == s[i+1]:
            table[i][i+1] = True
            start = i
            maxLen = 2

    for k in range(3, n):
        for i in range(0, n-k+1):
            j = i + k - 1
            if (table[i+1][j-1] == True and s[i] == s[j]):
                table[i][j] = True
                if (k > maxLen):
                    maxLen = k
                    start = i
                    #print " Found palin = ", s[start:start + maxLen]
    #print " start = ", i, " and maxLen = ", maxLen
    return s[start:start + maxLen]

if __name__ == "__main__":
    print " Run 1 : "
    s = "abcdefed"
    print longestPalindromeGFG(s)
    print " Run 2 : "
    s = "aaaa"
    print longestPalindromeGFG(s)
    print " Run 3 : "
    s = "abcda"
    print longestPalindromeGFG(s)
    print " Run 4 : "
    s = "aaaabaaa"
    print longestPalindromeGFG(s)