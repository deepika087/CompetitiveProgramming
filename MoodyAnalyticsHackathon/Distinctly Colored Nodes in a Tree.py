
def travelDownwards(travelDown, tree, C , seenColor, avoidNode):
    print "Received request for ", travelDown
    if (travelDown == avoidNode ):
        return
    elif (tree[travelDown-1][1] == 0 and tree[travelDown-1][2] == 0) :
        print "Looking for color of node : " , travelDown
        if ( C[travelDown - 1] not in seenColor):
            seenColor.append(C[travelDown - 1])
    else:
        print "Looking for color of node : " , travelDown
        if (travelDown != avoidNode and C[travelDown - 1] not in seenColor):
            seenColor.append(C[travelDown - 1])

        if (tree[travelDown-1][1] != 0):
            travelDownwards(tree[travelDown-1][1], tree, C, seenColor, avoidNode)
        if (tree[travelDown-1][2] != 0):
            travelDownwards(tree[travelDown-1][2], tree, C, seenColor, avoidNode)

        return seenColor

def getParent(node, tree):

    while (tree[node-1][3]!= 0):
        node = tree[node - 1][3]

    return node

if __name__=="__main__":
    N = int(raw_input(''))
    C = raw_input('')
    C = C.split()
    edges = []
    for i in range(0, N-1):
        line = raw_input('')
        edges.append(line.split())
    #print edges

    tree = []
    for i in range(1, N+1):
        tree.append([i, 0, 0, 0])

    for edge in edges:
        U = int(edge[0])
        V = int(edge[1])

        if (tree[U-1][1] == 0): #Left root is empty
            tree[U-1][1] = V
        else:
            tree[U-1][2] = V # Else assign it as right child

        tree[V-1][3] = U # Assign U as parent of V-1 node
    #print tree
    final = 0
    for edge in edges:
        print "================> For edge = ", edge
        travelUp = int(edge[0])
        travelDown = int(edge[1])

        seenColor = [ C[travelDown-1] ]

        result = travelDownwards(travelDown, tree, C, seenColor, travelUp) # Get the colors from it's childer

        D2 = len(seenColor)
        D1 = 0
        seenColor = []
        parent = getParent(travelUp, tree)
        print "Parent = ", parent
        print "Starting travelDownwards New"
        seenColor = travelDownwards ( parent, seenColor, tree, C, travelUp)
        D1 = len(seenColor) if seenColor is not None else 0
        print "D1 = ", D1
        final = final + (D1 * D2)
    print final