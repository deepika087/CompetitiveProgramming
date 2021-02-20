__author__ = 'deepika'

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """

        elements = [ (S.count(x), x) for x in set(S)]
        print(elements)
        output = []
        self.build_heap(elements)


        while len(elements) > 0:
            pop1 = elements.pop(0) #Max is at front

            if len(output) == 0 or output[-1] != pop1[1]:
                output.append(pop1[1])
                if pop1[0] - 1 > 0:
                    elements.append((pop1[0]-1, pop1[1]))
                    self.bubbleup(elements, len(elements)-1)
            elif output[-1] == pop1[1]: #Last element is the same
                if (len(elements) == 0):
                    return ""
                else:
                    pop2 = elements.pop(0)
                    output.append(pop2[1])
                    elements.append((pop1[0], pop1[1]))
                    self.bubbleup(elements, len(elements)-1)
                    if pop2[0]-1 > 0:
                        elements.append((pop2[0]-1, pop2[1]))
                        self.bubbleup(elements, len(elements)-1)
            else:
                print("Unhandled case")
        return ''.join(output)

    def build_heap(self, elements):
        for i in range(len(elements)/2, -1, -1):
            self.heapify(elements, i)

    def heapify(self, elements, i):
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l < len(elements) and elements[l][0] > elements[i][0]:
            largest = l
        if r < len(elements) and  elements[r][0] > elements[largest][0]:
            largest = r

        if largest != i:
            elements[i], elements[largest] = elements[largest], elements[i]
            self.heapify(elements, largest)


    def bubbleup(self, elements, i):
        parentIdx = (i - 1)/2
        currentIdx = i
        while currentIdx > 0 and elements[parentIdx][0] < elements[currentIdx][0]:

            elements[currentIdx], elements[parentIdx] = elements[parentIdx], elements[currentIdx]
            currentIdx = parentIdx;
            parentIdx = parentIdx/2;

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2





s=Solution()
#print(s.reorganizeString("aabcdabcbbbeee"))
#print(s.reorganizeString("aab"))
#print(s.reorganizeString("aaab"))
print(s.reorganizeString("blflxll")) # Expected: "lblflxl"