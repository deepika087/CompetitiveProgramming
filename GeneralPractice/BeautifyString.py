__author__ = 'deepika'


"""
this problem is the simpler verison of beautification of text.
There is one more version where the output for "abcdefghi"
for intervals = [ [ 0, 4, 'b'], [ 2, 6, 'i'] ]
will be         <b>ab<i>cd</i></b><i>ef</i>ghi
instead of this <b>ab<i>cd</b>ef</i>ghi

Step 1: close what all tags you can and specific i. because for interval (2, 4) the closing tag should come before string[4]
Step 2: Open all the tags opening at 'i'
Step 3: Till you don't find next interval just add to string.

"""
class Solution:

    def _fetchOpeningTag(self, character):
        return "<" + character + ">"

    def _fetchClosingTag(self, character):
        return "</" + character + ">"

    def beautify(self, string, intervals):

        i = 0 #Handles the string
        j = 0 #Traverses the intervals
        result = []
        stack = []
        intervals = sorted(intervals)

        while i < len(string):
            print ("result so far : ", ''.join(result), " with stack : ", stack)

            while len(stack) > 0 and i == stack[0][0]:
                popped = stack.pop(0)
                result.append(self._fetchClosingTag( popped[1] )) # put the closing tag

            while j < len(intervals) and i == intervals[j][0]:
                result.append(self._fetchOpeningTag(intervals[j][2]))
                stack.append( [intervals[j][1], intervals[j][2]] )
                j += 1

            if (j < len(intervals) and i < intervals[j][0]) or  ( j >= len(intervals)):
                result.append(string[i])
                i += 1

        while len(stack) > 0: #there might be left over tokens.
            popped = stack.pop()
            result.append(self._fetchClosingTag( popped[1] )) # put the closing tag

        return ''.join(result)



s=Solution()
intervals = [
    [ 0, 4, 'b'],
    [ 2, 6, 'i'],
]
#print(s.beautify("abcdefghi", intervals))
print(s.beautify("abc", [ [0, 1, 'b'], [1, 2, 'b'], [2, 3, 'b']]))
print(s.beautify("abc", [ [0, 3, 'b']]))