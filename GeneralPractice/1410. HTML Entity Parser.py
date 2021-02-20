__author__ = 'deepika'

"""
Runtime: 704 ms, faster than 30.98% of Python online submissions for HTML Entity Parser.
Memory Usage: 16.1 MB, less than 5.63% of Python online submissions for HTML Entity Parser.
"""
class Solution(object):
    def __init__(self):
        self.data = {
            "quot": "#",
            "apos" : "'" ,
            "amp" : "&",
            "gt" : ">",
            "lt" : "<",
            "frasl": "/"
        }

    def entityParser(self, text):
        """
        :type text: str
        :rtype: str
        """

        result = []
        save = -1
        for i in range(len(text)):
            if text[i] == '&':
                save = i+1
            elif text[i] == ";" and save != -1:
                string = text[save:i]
                save = -1
                if string in self.data:
                    result.append(self.data[string] if self.data[string] != "#" else ' \\" ')
                else:
                    result.append("&" + string + ";") #something like &ambassador;
            elif save == -1: #If any & has not been seen so far only then add
                result.append(text[i])

        return "".join(result)

s=Solution()
print(s.entityParser("&amp; is an HTML entity but &ambassador; is not."))
print(s.entityParser("and I quote: &quot;...&quot;"))
print(s.entityParser("Stay home! Practice on Leetcode :)"))
print(s.entityParser("x &gt; y &amp;&amp; x &lt; y is always false"))
print(s.entityParser("leetcode.com&frasl;problemset&frasl;all"))


