import sys
import copy

ZERO='0'
ONE='1'
TWO='2'

class AlphaBeta:
    def __init__(self, matrix, player, depth, cutOffDepth=10):
        self.matrix = matrix
        self.player = player
        self.oponent = '2' if self.player == '1' else '1'
        self.children = list()
        self.value = 0
        self.depth = depth
        self.cutOffDepth = cutOffDepth
        self.nextBoardState = None

    def getEvaluation(self): #Player has won 100. Oponent has won 50 else 0

        #Check is row win
        for i in range(3):
            if (self.matrix[i] == [self.player] * 3):
                return 100
            if (self.matrix[i] == [self.oponent] * 3):
                return 0

        #column win
        for i in range(3):
            col = list()
            for j in [0, 1, 2]:
                col += self.matrix[j][i]
            if (col == [self.player] * 3):
                return 100
            if (col == [self.oponent] * 3):
                return 0

        #diagonal win
        for i in range(3):
            diag = list()
            for j in range(3):
                diag += self.matrix[i][j]

            if (diag == [self.player] * 3):
                return 100
            if (diag == [self.oponent] * 3):
                return 0

        #off diagonal win

        for i in range(3):
            offdiag = list()
            for j in range(3):
                if ( i + j == 2):
                    offdiag += self.matrix[i][j]
                    break
            if (offdiag == [self.player] * 3):
                return 100
            if (offdiag == [self.oponent] * 3):
                return 0
        return 50 #In case of draw

    def printGrid(self):
        for i in range(3):
            for j in range(3):
                print self.matrix[i][j], ", "
            print "\n"

    def startRunning(self):
        alpha = -sys.maxint
        beta = sys.maxint
        self.startRunning_Util(alpha, beta)
        #print ' RESULT : '
        return self.getDifference()
        #print self.nextBoardState

    def getDifference(self): #We have to find difference between boartstate and next state of boardstate

        for i in range(3):
            for j in range(3):
                if (self.matrix[i][j] == self.nextBoardState.matrix[i][j]):
                    continue
                else:
                    return i,j

    def __repr__(self):
        lineOfGrid = ""
        for i in range(3):
            lineOfGrid += ''.join(self.matrix[i]) + "\n"
        return lineOfGrid

    def __str__(self):
        return self.__repr__()

    def startRunning_Util(self, alpha, beta):
        children = self.findStates() #List<BoardStates>
        #print " running for state : ", self.matrix
        #print "Possible number of child in this case : ", len(children)

        #self.custom_print(children)

        if (self.depth == self.cutOffDepth or len(children) == 0):
            self.value = self.getEvaluation()
            return self.value

        if (self.depth % 2 == 0): #Maximizer
            self.value = -sys.maxint
            for child in children:
                child_v = child.startRunning_Util(alpha, beta)
                self.value = max(self.value, child_v)

                if (self.value >= beta):
                    #print " Pruning "
                    return child_v
                if (self.value > alpha):
                    self.nextBoardState = child
                alpha = max(alpha, self.value)
            #return self.value
        else:
            self.value = sys.maxint
            for child in children:
                child_v = child.startRunning_Util(alpha, beta)
                self.value = min(self.value, child_v)
                if (self.value <= alpha):
                    #print " Prunning the branch at node : ", child.value
                    return child_v
                if (self.value < beta):
                    self.nextBoardState = child
                beta = min(beta, child_v)
        return self.value


    def custom_print(self, children): #children = List<AlphaBeta>
        customLines = ""
        for i in range(3):
            for child in children:
                customLines += child.matrix[i] + " | "
            customLines += "\n"
        print customLines


    def findStates(self): #Given matrix and player find the next legal moves
        boardStates = list() #List<BoardStates> or List<AlphaBeta> exactly
        handledCoordinates = set()
        noOfOpponent = 0
        noOfPlayer = 0
        flag = True
        for i in range(3):
            for j in range(3):
                if (self.matrix[i][j] == self.oponent):
                    noOfOpponent = noOfOpponent + 1
                    flag = False
                    boardStates+= self.getValidNeighbours(i, j, handledCoordinates)
        if (flag): #No occurence of opponent as of now then block the next moves of self.player
            for i in range(3):
                for j in range(3):
                    if (self.matrix[i][j] == self.player):
                        noOfPlayer = noOfPlayer + 1
                        flag = False
                        boardStates+= self.getValidNeighbours(i, j, handledCoordinates)
        if (noOfOpponent == 0 and noOfPlayer == 0 ):
            boardStates+= self.getValidNeighbours(-1, -1, handledCoordinates)

        return boardStates

    def getValidNeighbours(self, i, j, handledCoordinates):
        validStates = list() #List<BoardStates>
        #matrix2 = copy.copy(self.matrix)

        if (i-1 >= 0): #For the row above there are 3 possible moves

            if (j-1 >= 0 and self.matrix[i-1][j-1] == ZERO and (i-1, j-1) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i-1]
                route = list(route)
                route[j-1] = self.oponent
                matrix2[i-1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i-1, j-1))
            if (j >= 0 and self.matrix[i-1][j] == ZERO and (i-1, j) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i-1]
                route = list(route)
                route[j] = self.oponent
                matrix2[i-1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i-1, j))
            if (j+1 < 3 and self.matrix[i-1][j+1] == ZERO and (i-1, j+1) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i-1]
                route = list(route)
                route[j+1] = self.oponent
                matrix2[i-1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i-1, j+1))
        if ( i+1 < 3):
            if (j-1 >= 0 and self.matrix[i+1][j-1] == ZERO and (i+1, j-1) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i+1]
                route = list(route)
                route[j-1] = self.oponent
                matrix2[i+1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i+1, j-1))
            if (j>=0 and self.matrix[i+1][j] == ZERO and (i+1, j) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i+1]
                route = list(route)
                route[j] = self.oponent
                matrix2[i+1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i+1, j))
            if (j+1 < 3 and self.matrix[i+1][j+1] == ZERO and (i+1, j+1) not in handledCoordinates):
                matrix2 = copy.copy(self.matrix)
                route = matrix2[i+1]
                route = list(route)
                route[j+1] = self.oponent
                matrix2[i+1] = ''.join(route)
                validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
                handledCoordinates.add((i+1, j+1))
        if (j-1 >= 0 and self.matrix[i][j-1] == ZERO and (i, j-1) not in handledCoordinates):
            matrix2 = copy.copy(self.matrix)
            route = matrix2[i]
            route = list(route)
            route[j-1] = self.oponent
            matrix2[i] = ''.join(route)
            validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
            handledCoordinates.add((i, j-1))
        if ( j+1 < 3 and self.matrix[i][j+1] == ZERO and (i, j+1) not in handledCoordinates):
            matrix2 = copy.copy(self.matrix)
            route = matrix2[i]
            route = list(route)
            route[j+1] = self.oponent
            matrix2[i] = ''.join(route)
            validStates.append(AlphaBeta(matrix2, self.oponent, self.depth+1))
            handledCoordinates.add((i, j+1))

        return validStates

if __name__ == "__main__":
    matrixLines = list()
    nextPlayer = -1

    count = 0;
    """
    for line in open("TTT_input.txt", 'r'):
        if (count < 3):
            line1 = line.strip()
            line1 = line1.split(' ')
            line1 = ''.join(line1)
            matrixLines.append(line1)
            count = count + 1
        else:
            nextPlayer = line.strip()
            break;
    """
    for i in range(3):
        line1 = raw_input('')
        line1 = line1.strip()
        line1 = line1.split(' ')
        line1 = ''.join(line1)
        matrixLines.append(line1)

    nextPlayer = int(raw_input(''))

    boardCurrent = AlphaBeta(matrixLines, '2' if nextPlayer == '1' else '1', depth=0)
    #print boardCurrent
    i, j = boardCurrent.startRunning()
    #print i, j
    #print " BReak at ",i, j
    if ((i,j) == (0,0) or (i,j) == (1,1) or (i,j) == (2,2)):
        print i,j
    else:
        print j,i