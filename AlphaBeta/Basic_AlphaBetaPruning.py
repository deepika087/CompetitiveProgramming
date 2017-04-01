__author__ = 'deepika'

import sys

PLAYER1 = 1
PLAYER2 = 2

class Node:
    def __init__(self, value=0):
        self.value = value
        self.alpha = 0
        self.beta = 0
        self.children = list()

    def printFromLeftToRight(self):
        if (len(self.children) == 0):
            print self.value
            return

        for i in range(len(self.children)):
            self.children[i].printFromLeftToRight()

        print self.value

    def isLeaf(self):
        return len(self.children) == 0

    def startRunning_Util(self, alpha, beta, player):
        if (self.isLeaf()):
            print " Hit the leaf node :", self.value
            return self.value

        if (player == PLAYER1): #Max Player, Actions here is equivalent of children
            self.value = -sys.maxint
            for child in self.children:
                child_v = child.startRunning_Util(alpha, beta, PLAYER2)
                #print " received child value : ", child_v
                self.value = max(self.value, child_v)

                #print " Comparing v and beta ", self.value, beta
                if (self.value >= beta):
                    print " Cutting the branch from this node on : ", child.value
                    return child_v
                alpha = max(alpha, self.value)
                #print " At node : ", child.value, " updated alpha = ", alpha
            return self.value
        else:
            self.value = sys.maxint
            for child in self.children:
                child_v = child.startRunning_Util(alpha, beta, PLAYER1)
                self.value = min(self.value, child_v)
                if (self.value <= alpha):
                    print " Prunning the branch at node : ", child.value
                    return child_v
                beta = min(beta, child_v)
            return self.value


class AlphaBeta:
    def __init__(self, tree):
        self.tree = tree

    def startRunning(self, player):
        alpha = -sys.maxint
        beta = sys.maxint
        return self.tree.startRunning_Util(alpha, beta, player)



if __name__ == "__main__":
    #Level 1 nodes
    main=Node()

    #Level 2 nodes
    children1 =  main.children
    children1.append(Node())
    children1.append(Node())

    #Level 3 nodes
    children1[0].children.append(Node(2))
    children1[0].children.append(Node(3))
    children1[1].children.append(Node(1))
    children1[1].children.append(Node(5))

    #level 4 nodes
    children1[0].children[0].children.append(Node())
    children1[0].children[0].children.append(Node())
    children1[0].children[1].children.append(Node())
    children1[0].children[1].children.append(Node())
    children1[1].children[0].children.append(Node())
    children1[1].children[0].children.append(Node())
    children1[1].children[1].children.append(Node())
    children1[1].children[1].children.append(Node())

    #Level 5 nodes
    children1[0].children[0].children[0].children.append(Node(3))
    children1[0].children[0].children[0].children.append(Node(17))
    children1[0].children[0].children[1].children.append(Node(2))
    children1[0].children[0].children[1].children.append(Node(12))
    children1[0].children[1].children[0].children.append(Node(15))
    #children1[0].children[1].children[0].append(Node(17))
    children1[0].children[1].children[1].children.append(Node(25))
    children1[0].children[1].children[1].children.append(Node(0))

    children1[1].children[0].children[0].children.append(Node(2))
    children1[1].children[0].children[0].children.append(Node(5))
    children1[1].children[0].children[1].children.append(Node(3))
    #children1[1].children[0].children[1].append(Node(12))
    children1[1].children[1].children[0].children.append(Node(2))
    children1[1].children[1].children[0].children.append(Node(14))
    #children1[1].children[1].children[1].append(Node(25))
    #children1[1].children[1].children[1].append(Node(0))

    print " Leaf nodes from left to "
    main.printFromLeftToRight()

    start_player = PLAYER1 #maximizer

    alphaBeta = AlphaBeta(main)
    result = alphaBeta.startRunning(start_player)
    print "Max value of the tree : ", result

    print " Print again (Left - Right - Node manner/Preorder traversal):"
    main.printFromLeftToRight()