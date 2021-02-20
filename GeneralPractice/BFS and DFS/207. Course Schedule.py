__author__ = 'deepika'

"""
Runtime: 84 ms, faster than 80.37% of Python online submissions for Course Schedule.
Memory Usage: 14.1 MB, less than 87.82% of Python online submissions for Course Schedule.

Say courses are like this 1->2->3->4

So, your preReq map will look like this 1 -> 2, 2 -> 3, 3 ->4
preReq map is a outdegree map.
Another way to look at it is that given a key we can find what all courses depend on it.

That is why we need another data structure for the in-degree map.

time and Space complexity = O(V + E) is same as order N

"""

class Solution(object):
    def dataRepresentation(self, numCourses, prerequisites):
        preReqs = dict()
        in_degree = [ 0 for i in range(numCourses)]

        for i in range(numCourses):
            preReqs[i] = []
        for pre in prerequisites:
            if pre[1] in preReqs:
                preReqs[pre[1]].append(pre[0])
            in_degree[pre[0]] += 1

        return preReqs, in_degree

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        preReqs, in_degree = self.dataRepresentation(numCourses, prerequisites)

        """
        Basically PreReq is a outdegree hashmap. so, len(v) is not the indegree
        """
        queue = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                queue.append(i)

        visited = set()
        result = []


        while len(queue) > 0:
            popped = queue.pop(0)
            visited.add(popped)

            for neighbour in preReqs[popped]:
                if neighbour in visited:
                    continue

                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

            result.append(popped)
            del preReqs[popped]

        return len(result) == numCourses
        # to fetch teh actual result
        # return result if len(result) == numCourses else []

s=Solution()
#print(s.canFinish(numCourses = 2, prerequisites = [[1,0]]))
#print(s.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
#print(s.canFinish(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
print(s.canFinish(numCourses = 3, prerequisites = [[1,0],[1,2],[0,1]]))

