__author__ = 'deepika'


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        result = [0 for i in range(len(T))]
        stack = [] #stack of indices

        i = 0
        while i < len(T):
            if len(stack) == 0:
                stack.append(i)
                i = i + 1
            else:
                incoming = T[i]
                topIndex = stack.pop()

                while topIndex != -1  and incoming > T[topIndex]:
                    result[topIndex] = i - topIndex
                    if (len(stack) > 0):
                        topIndex = stack.pop()
                    else:
                        topIndex = -1
                if incoming <= T[topIndex]:
                    stack.append(topIndex)

                stack.append(i)
                i = i + 1


        return result

s=Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(s.dailyTemperatures([1,3,4,2]))