__author__ = 'deepika'

"""
Runtime: 1380 ms, faster than 86.78% of Python online submissions for Time Needed to Inform All Employees.
Memory Usage: 33.2 MB, less than 90.97% of Python online submissions for Time Needed to Inform All Employees.
"""
class Solution(object):
    def getRepresentation(self, manager, headID):
        hierarchy = dict()

        for i in range(len(manager)):
            if manager[i] == -1:
                #hierarchy[-1] = i
                continue
            if manager[i] not in hierarchy:
                hierarchy[manager[i]] = []
            hierarchy[manager[i]].append(i)
        return hierarchy

    def startAnnouncing(self, hierarchy, headID, informTime):

        if headID not in hierarchy:
            return 0
        to_this_level = informTime[headID] + max([ self.startAnnouncing(hierarchy, manager, informTime) for manager in hierarchy[headID] ] )
        return to_this_level


    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """

        if n == 0 or n == 1:
            return 0
        count = 0

        hierarchy = self.getRepresentation(manager, headID)
        count += self.startAnnouncing(hierarchy, headID, informTime)
        return count

s=Solution()
print(s.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
print(s.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))
print(s.numOfMinutes(n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]))
print(s.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [0]))
print(s.numOfMinutes(8, 0, [-1,5,0,6,7,0,0,0], [89,0,0,0,0,523,241,519]))