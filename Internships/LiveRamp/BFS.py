
"""
Liveramp qs taken from online source. However, I was not asked any question as mentioned on glassdoor
"""
def bfs(graph, start, end):
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[0]

        for item in graph[node] - set(path):
            print "Exploring for item", item
            new_path = [item]
            new_path += path
            queue.append(new_path)
            print "Appending" , new_path
            if (item == end):
                return "Length = " + str(len(new_path)) + " PATH = " + str(new_path)


if __name__=="__main__":
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
    print bfs(graph, 'A', 'E')