"""
Accepted.
39 ms
Beats 67.65%
Traverses the graph just once.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        oldToNew = defaultdict(Node)
        seen_nodes = set()  # has a specific node been a source
                            # n1 -> n2, n3
                            # We will put n1 to seen only when we have seen it as source to certain destinations
        while stack:
            popped = stack.pop(-1)
            if popped not in seen_nodes:
                if popped not in oldToNew:
                    oldToNew[popped] = Node(popped.val)
                seen_nodes.add(popped)

                for neighbour in popped.neighbors:
                    if neighbour not in oldToNew:
                        oldToNew[neighbour] = Node(neighbour.val)
                    stack.append(neighbour)
                    oldToNew[popped].neighbors.append(oldToNew[neighbour])
        return oldToNew[node]
