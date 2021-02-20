_author__ = 'deepika'

"""
apply DP this one give TLE
"""
class Solution(object):
    def __init__(self):
        self.count = 0

    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """

        if len(locations) == 0:
            return 0

        self.startDFS(start, finish, fuel, locations)
        save = self.count
        self.count = 0
        return save

    def startDFS(self, start, finish, fuel, locations):
        if start < 0 or start >= len(locations) or fuel < 0:
            return 0

        if start == finish:
            self.count += 1
            self.count %= (10^9 + 7)

        for j in range(len(locations)):
            if j == start:
                continue
            self.startDFS(j, finish, fuel - abs(locations[j] - locations[start]), locations)

s=Solution()
assert s.countRoutes(locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5) == 4
assert s.countRoutes(locations = [4,3,1], start = 1, finish = 0, fuel = 6) == 5
assert s.countRoutes(locations = [5,2,1], start = 0, finish = 2, fuel = 3) == 0
assert s.countRoutes(locations = [2,1,5], start = 0, finish = 0, fuel = 3) == 2
print("done")
assert s.countRoutes(locations = [1,2,3], start = 0, finish = 2, fuel = 40) == 615088286