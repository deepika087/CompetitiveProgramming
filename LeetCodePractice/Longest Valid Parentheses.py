class Solution(object):
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        mystack = []
        count = 0
        for i in s:

            if (i == ')' ):
                if (len(mystack) == 0):
                    continue
                elif (mystack[-1] == '()'):
                    continue
                elif(mystack[-1] == '('):
                    mystack.pop(-1)
                    mystack.append('()')
            elif ( i == '('):
                mystack.append(i)
        print mystack
        while(len(mystack) > 0):
            if (mystack.pop(-1) == '()'):
                count = count + 2
            else:
                break
        return count

    def longestValidParentheses(self, s):
        start = 0
        end = 0;
        i = 0
        saveStart = -1
        saveEnd = -1
        saveLen = -1
        while( i < len(s)):
            while ( i < len(s) and s[i] == ')'):
                i = i + 1
            #This is the point of first opening brace

            start = i
            end = i

            while(i < len(s) and s[i] == '('):
                i = i + 1
            end = i#this is the first occurrence of ')
            i = i - 1
            while(end < len(s) and s[end] == ')' and i > 0):
                if (end + 1 < len(s)):
                    end = end + 1
                i = i - 1
            if (saveStart == -1 and saveEnd == -1):
                saveStart = i
                saveEnd = end - 1
            else:
                if ( i == saveEnd + 1): #Candidate of merge
                    saveEnd = end - 1 #savestart remains the same
                else:
                    prevLen = saveEnd - saveStart
                    newlen = end - 1 - i
                    if ( newlen > prevLen):
                        saveStart = i
                        saveEnd = end - 1
            i = i + end
            if (saveStart == 0):
                print "1.start = ", saveStart, " and end = ", saveEnd
                return (saveEnd - saveStart + 1) /2
        print "2. start = ", saveStart, " and end = ", saveEnd
        return saveEnd - saveStart


s=Solution()
print s.longestValidParentheses("(()")
print s.longestValidParentheses("()")
print s.longestValidParentheses(")()())")
print s.longestValidParentheses("()(()") #expected 2
print s.longestValidParentheses("()(())")