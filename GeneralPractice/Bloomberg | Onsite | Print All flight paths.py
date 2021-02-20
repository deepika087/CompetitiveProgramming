__author__ = 'deepika'


class Solution:

    def __init__(self):
        self.flights = dict()

    #Assuming that we will not try to add S -> D mapping such that S -> D already exists in the dictionary.
    def addStops(self, source, destination):

        if source not in self.flights:
            self.flights[source] = []
        self.flights[source].append(destination)

    #Handles cycles as well using visited set()
    def fetchPaths(self, source, destination):

        visited = set()
        visited.add(source)

        path_so_far = [source]

        self.fetchPathsUtil(source, destination, path_so_far, visited)

    def fetchPathsUtil(self, source, destination, path_so_far, visited):

        if path_so_far[-1] == destination:
            print("->".join(path_so_far))
            return

        for city in self.flights[source]:
            if city not in visited:
                path_so_far.append(city)
                visited.add(city)
                self.fetchPathsUtil(city, destination, path_so_far, visited)

                visited.remove(city)
                path_so_far.pop(-1)


s=Solution()
s.addStops('A', 'B')
s.addStops('A', 'P')
s.addStops('P', 'E')
s.addStops('B', 'C')
s.addStops('B', 'D')
s.addStops('C', 'G')
s.addStops('C', 'A')
s.addStops('G', 'E')
s.addStops('C', 'E')
s.addStops('D', 'E')
s.addStops('E', 'P')
s.fetchPaths('A', 'E')