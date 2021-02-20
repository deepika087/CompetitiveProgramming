__author__ = 'deepika'


class Solution:

    def traverse(self, string):

        idx = -1
        result = []
        curr_string = ""
        self.traverseUtil(string, idx, result, curr_string)
        print(result)

    def traverseUtil(self, string, idx, result, curr_string):

        if idx >= len(string):
            return

        result.append(''.join(curr_string))

        for i in range(idx+1, len(string)):
            curr_string += string[i]
            print("Beginning string: ", curr_string)
            self.traverseUtil(string, i, result, curr_string)
            #curr_string.pop()
            curr_string = curr_string[:len(curr_string) - 2] # Basically pop the last element.
        return


s=Solution()
s.traverse("abc")