__author__ = 'deepika'


from heapq import heappop, heappush


class Solution:
    def maxEvents(self, events):
        events.sort(key=lambda x : x[1])
        book,res=set(),0
        for s,e in events:
            i=s
            while i in book and i<=e:
                i+=1
            if i<=e:
                res+=1
                book.add(i)
        return res
s=Solution()
print(s.maxEvents( [ [1, 10], [2, 3], [4, 5], [6, 7] ] ))