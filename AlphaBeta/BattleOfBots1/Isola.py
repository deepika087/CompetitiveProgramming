
import sys
import copy

ZERO='0'
ONE='1'
TWO='2'
EMPTY='-1'

class AlphaBeta:
    def __init__(self, matrix, player, depth, cutOffDepth=10):
        self.matrix = matrix
        self.player = player
        self.oponent = '2' if self.player == '1' else '1'
        self.value = 0
        self.depth = depth
        self.cutOffDepth = cutOffDepth
        self.nextBoardState = None

    def getEvaluation(self):
        pass

    def __repr__(self):
        lineOfGrid = ""
        for i in range(7):
            lineOfGrid += ''.join(self.matrix[i]) + "\n"
        return lineOfGrid

    def __str__(self):
        return self.__repr__()

    def custom_print(self, children): #children = List<AlphaBeta>
        customLines = ""
        for i in range(7):
            for child in children:
                customLines += child.matrix[i] + " | "
            customLines += "\n"
        print customLines

    def startRunning(self):
        alpha = -sys.maxint
        beta = sys.maxint
        print self.matrix
        #self.startRunning_Util(alpha, beta)
        #print ' RESULT : '
        #return self.getDifference()

    def startRunning_Util(self, alpha, beta):
        children = self.findStates() #List<BoardStates>

        if (self.depth == self.cutOffDepth or len(children) == 0):
            self.value = self.getEvaluation()
            return self.value

        if (self.depth % 2 == 0): #Maximizer
            self.value = -sys.maxint
            for child in children:
                child_v = child.startRunning_Util(alpha, beta)
                self.value = max(self.value, child_v)

                if (self.value >= beta):
                    return child_v
                if (self.value > alpha):
                    self.nextBoardState = child
                alpha = max(alpha, self.value)
        else:
            self.value = sys.maxint
            for child in children:
                child_v = child.startRunning_Util(alpha, beta)
                self.value = min(self.value, child_v)
                if (self.value <= alpha):
                    return child_v
                if (self.value < beta):
                    self.nextBoardState = child
                beta = min(beta, child_v)
        return self.value


if __name__ == "__main__":
    matrixLines = list()
    nextPlayer = -1

    count = 0;

    #For debugging purpose input from files only
    for line in open("isola_input.txt", 'r'):
        if (count < 7):
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
    """
    boardCurrent = AlphaBeta(matrixLines, '2' if nextPlayer == '1' else '1', depth=0)
    #print boardCurrent
    i, j = boardCurrent.startRunning()
    #print i, j
    #print " BReak at ",i, j
    print i, i