__author__ = 'deepika'

"""
This problem is different from Apple problem cz ther if we encounter deadend. We can just mark it as we don't want to visit it again.
However, here that is not the case so recursion looks like the best option
class Solution {

    public boolean exist (char[][] board, String word) {
        ArrayList <Integer> startX = new ArrayList ();
        ArrayList <Integer> startY = new ArrayList ();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board [i][j] == word.charAt (0)) {
                    startX.add (i);
                    startY.add (j);
                }
            }
        }
        boolean visited [][] = new boolean [board.length][board[0].length];
        if (startX.size () == 0)
            return false;
        for (int i = 0; i < startX.size (); i++) {
            int x = startX.get (i);
            int y = startY.get (i);
            if (Solve (board, word, x, y, 0, visited))
                return true;
        }
        return false;
    }

    public boolean Solve (char grid [][], String S, int x, int y, int index, boolean visited [][]) {
        if (index >= S.length ())
            return true;
        if (!isValid (grid, x, y, S.charAt (index), visited))
            return false;
        visited [x][y] = true;
        if (Solve (grid, S, x + 1, y, index + 1, visited))
            return true;
        if (Solve (grid, S, x, y + 1, index + 1, visited))
            return true;
        if (Solve (grid, S, x - 1, y, index + 1, visited))
            return true;
        if (Solve (grid, S, x, y - 1, index + 1, visited))
            return true;
        visited [x][y] = false;
        return false;
    }

    public boolean isValid (char grid [][], int x, int y, char ch, boolean visited [][]) {
        if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length && visited [x][y] == false && grid [x][y] == ch)
            return true;
        return false;
    }
}

"""

class Solution(object):

    def scanForFirstChar(self, board, character):
        inputList = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == character:
                    inputList.append( (i, j) )
        return inputList

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(word) == 0:
            return False

        index = 0
        inputList = self.scanForFirstChar(board, word[index])
        if len(inputList) == 0:
            return False

        for _input in inputList:

            stack = []
            visited= []

            stack.append(_input)
            result = self.startDFS(board, stack, visited, index + 1, word)
            if result:
                return True

    def isvalidcoordinate(self, i, j, m, n):
        return i >= 0 and j >= 0 and i < m and j < n

    def getNeighbours(self, board, inputCoordinate, character, visited ):

        neighbours = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue

                iDelta = inputCoordinate[0] + i
                jDelta = inputCoordinate[1] + j

                if self.isvalidcoordinate(iDelta, jDelta, len(board), len(board[0])):
                    if ((iDelta, jDelta) not in visited and board[iDelta][jDelta] == character):
                        neighbours.append( (iDelta, jDelta) )
        return neighbours

    def startDFS(self, board, stack, visited, index, word):

        while len(stack) > 0:
            popped = stack.pop(-1)
            print("Gonna investigate", popped)

            if index == len(word) - 1 and board[popped[0]][popped[1]] == word[index]:
                print("returning")
                return True

            if index < len(word):
                neighbours = self.getNeighbours(board, popped, word[index], visited)
                print("Neighbours" , neighbours)
                if len(neighbours) == 0 and index > 0 and index < len(word): # Deadend
                    print("Deadend. go back")
                    visited.append( (popped[0], popped[1]) )
                    index -= 1
                    continue
                stack += [popped]
                stack.extend(neighbours)
                print("New stack: ", stack)
                index += 1

                visited.append(popped)
        return False

s=Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(s.exist(board, "ABCCED"))
"""

('Gonna investigate', (0, 0))
('Neighbours', [(0, 1)])
('New stack: ', [(0, 0), (0, 1)])
('Gonna investigate', (0, 1))
('Neighbours', [(0, 2), (1, 2)])
('New stack: ', [(0, 0), (0, 1), (0, 2), (1, 2)])
('Gonna investigate', (1, 2))
('Neighbours', [(0, 2)])
('New stack: ', [(0, 0), (0, 1), (0, 2), (1, 2), (0, 2)])
('Gonna investigate', (0, 2))
('Neighbours', [(0, 3)])
('New stack: ', [(0, 0), (0, 1), (0, 2), (1, 2), (0, 2), (0, 3)])
('Gonna investigate', (0, 3))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (0, 2))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (1, 2))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (0, 2))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (0, 1))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (0, 0))
('Neighbours', [])
('New stack: ', [(0, 0)])
('Gonna investigate', (0, 0))
('Neighbours', [])
Deadend. go back
('Gonna investigate', (2, 0))
('Neighbours', [])
Deadend. go back
None


"""

#print(s.exist(board, "SEE"))
#print(s.exist(board, "ABCB"))



