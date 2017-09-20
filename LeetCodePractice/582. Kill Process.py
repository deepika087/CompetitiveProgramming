__author__ = 'deepika'

"""
166 / 166 test cases passed.
Status: Accepted
Runtime: 292 ms
Better than 92%
"""
# Follow DFS approach to delete the children
class Solution(object):

    def formDictionaries(self, pid, ppid):

        parent = dict()
        for idx in range(len(ppid)):
            _p = ppid[idx]
            if _p in parent:
                parent[_p].append(idx)
            else:
                parent[_p] = [idx]
        return parent

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        parent = self.formDictionaries(pid, ppid)
        print parent
        node_to_delete_idx = pid.index(kill)

        result, stack = [], [node_to_delete_idx]
        while stack:
            popped = stack.pop() #this is the idx and not the node itself
            if popped is None:
                continue
            node = pid[popped]
            result.append(node)

            if node in parent:
                stack += parent[node]
            print "Stack updated: ", stack
        return result

s=Solution()
assert s.killProcess([1], [0], 1) == [1]
assert( s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5) == [5, 10])