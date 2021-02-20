__author__ = 'deepika'

# Python3 implementation to
# find LCA in a tree
MAXN = 1001

# stores depth for each node
depth = [0 for i in range(MAXN)];

# stores first parent for each node
parent = [0 for i in range(MAXN)];

adj = [[] for i in range(MAXN)]

def addEdge(u, v):

    adj[u].append(v);
    adj[v].append(u);

def dfs(cur, prev):

    # marking parent for
    # each node
    parent[cur] = prev;

    # marking depth for
    # each node
    depth[cur] = depth[prev] + 1;

    # propogating marking down
    # the tree
    for i in range(len(adj[cur])):
        if (adj[cur][i] != prev): #if not going back to parent
            dfs(adj[cur][i], cur);

def preprocess():

    # a dummy node
    depth[0] = -1;

    # precalculating 1)depth.
    # 2)parent. for each node
    dfs(1, 0);

# Time Complexity : O(Height of tree)
# recursively jumps one node above
# till both the nodes become equal
def LCANaive(u, v):

    if (u == v):
        return u;

    if (depth[u] > depth[v]): #u, and v keeps toggling even when they are equalized first time.
        u, v = v, u

    v = parent[v];
    return LCANaive(u, v);

# Driver code
if __name__ == "__main__":

    # adding edges to the tree
    addEdge(1, 2);
    addEdge(1, 3);
    addEdge(1, 4);
    addEdge(2, 5);
    addEdge(2, 6);
    addEdge(3, 7);
    addEdge(4, 8);
    addEdge(4, 9);
    addEdge(9, 10);
    addEdge(9, 11);
    addEdge(7, 12);
    addEdge(7, 13);

    preprocess();

    print('LCA(11,8) : ' +
           str(LCANaive(11, 8)))
    print('LCA(3,13) : ' +
           str(LCANaive(3, 13)))
