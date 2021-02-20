__author__ = 'deepika'

#This method usses Topological sort
# This approach asusmes it is Directed acyclic graph
# as done by https://github.com/mission-peace/interview/blob/master/src/com/interview/graph/TopologicalSort.java
def sortProcess(process):

    result = [] #Act like stack
    visited = set()

    for vertice in process.keys():
        if vertice in visited:
            continue
        else:
            dfs(vertice, process, result, visited)
    return result

def dfs(startPoint, processes, result, visited):
    print "Vistied:", startPoint
    visited.add(startPoint)

    for neighbour in processes[startPoint]:
        if neighbour in visited:
            continue
        else:
            dfs(neighbour, processes, result, visited)
    result.append(startPoint)


print sortProcess(
    {
     'c' : [],
     'a' : [ 'b'] ,
     'g' : ['f'],
     'd' : ['c'],
     'e' : 'b',
     'f' : ['d', 'e'],
     'b' : ['c'],
    }
)

#['a', 'b', 'c', 'e', 'd', 'f', 'g']