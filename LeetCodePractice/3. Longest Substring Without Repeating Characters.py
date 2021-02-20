
"""
983 / 983 test cases passed.
Status: Accepted
Runtime: 129 ms
"""
class Solution(object):
    def lengthOfLongestSubstringOptimized(self, s):
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
        visited[0] = 1
        start = 0
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                visited[i] = 1
                character[s[i]] = i
                start = i # start is the potential of start point of unique window
            else:
                if ( character.get(s[i]) < start ): # This is the previous occrance of character.get(s[i])
                    visited[i] = visited[i-1] + 1 #Now the occurence of repeated char occured some time back that before start
                else:
                    visited[i] = i - character.get(s[i], 0)
                    start = character[s[i]] + 1 #new potential for new unique sub-string
                character[s[i]] = i #Update the position
        #print visited
        return max(visited)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print "Also going here"
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
            print "start: ", start
            if (s[i] not in seenChar):
                visited[i] = visited[i-1] + 1
                seenChar.append(s[i])
                character[s[i]] = i
            else:
                if (s[i] == s[i-1]):
                    visited[i] = 1
                    seenChar = [s[i]] #Reset everything
                    character[s[i]] = i
                    start = i # start is the potential of start point of unique window
                else:
                    if ( character.get(s[i]) < start ): # This is the previous occrance of character.get(s[i])
                        print "called for string: ", s, " character : ", s[i], character.get(s[i]), "start = ", start
                        visited[i] = visited[i-1] + 1 #Now the occurence of repeated char occured some time back that before start
                    else:
                        visited[i] = i - character.get(s[i], 0) # Basically current - prev occurence of this charcater.
                        start = character[s[i]] + 1 #new potential for new unique sub-string starting prev occurence of this char + 1
                        # hence we don't fix seenChar here. BEcause basically we are reusing that subset.
                    character[s[i]] = i

        #print visited
        return max(visited)


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstringNew("wobgrovw") == 6
    assert sol.lengthOfLongestSubstringNew("ckilbkd") == 5
    assert sol.lengthOfLongestSubstringNew("abcaaabcdefgh")== 8
    assert sol.lengthOfLongestSubstringNew("abcabcbb") == 3
    assert sol.lengthOfLongestSubstringNew("bbbbb") == 1
    assert sol.lengthOfLongestSubstringNew("pwwkew") == 3
    assert sol.lengthOfLongestSubstringNew("qwnfenpglqdq") == 8


