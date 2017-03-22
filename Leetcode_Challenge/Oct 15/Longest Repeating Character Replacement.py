
"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times.
Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        #find character with max occurence
        character = dict()
        max = 0
        for i in s:
            if (character.get(i, -1) == -1):
                character[i] = 1
            else:
                character[i] = character[i] + 1
            if (character[i] > max):
                max = character[i]

if __name__ == "__main__":
    sol = Solution()
    sol.characterReplacement("ABAB", 2)
    sol.characterReplacement("AABABBA", 1)
