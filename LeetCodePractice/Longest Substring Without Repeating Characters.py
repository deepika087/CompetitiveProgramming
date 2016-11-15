
"""
982 / 982 test cases passed.
Runtime: 208 ms
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0):
            return 0
        elif (len(s) == 1):
            return 1
        character = dict()
        character[s[0]] = 0
        visited = [ 0 for _ in range(len(s))]
        seenChar = [s[0]]
        visited[0] = 1
        start = 0
        for i in range(1, len(s)):
            if (s[i] not in seenChar):
                visited[i] = visited[i-1] + 1
                seenChar.append(s[i])
                character[s[i]] = i
            else:
                if (s[i] == s[i-1]):
                    visited[i] = 1
                    seenChar = [s[i]] #Reset everything
                    character[s[i]] = i
                    start = i
                else:
                    if ( character.get(s[i]) < start ): # This is the previous occrance of character.get(s[i])
                        visited[i] = visited[i-1] + 1
                    else:
                        visited[i] = i - character.get(s[i], 0)
                        start = character[s[i]] + 1
                    character[s[i]] = i

        #print visited
        return max(visited)


if __name__ == "__main__":
    sol = Solution()
    print sol.lengthOfLongestSubstring("wobgrovw") #expected 6
    print sol.lengthOfLongestSubstring("ckilbkd") #expected 5
    print sol.lengthOfLongestSubstring("abcaaabcdefgh") #expected 8
    print sol.lengthOfLongestSubstring("abcabcbb") #expected 3
    print sol.lengthOfLongestSubstring("bbbbb") #expected 1
    print sol.lengthOfLongestSubstring("pwwkew") #expected 3
    print sol.lengthOfLongestSubstring("qwnfenpglqdq") #expected 8


