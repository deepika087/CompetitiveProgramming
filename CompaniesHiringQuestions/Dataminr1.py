__author__ = 'deepika'

"""
Full Time experience: Oct 18, 2017

Xoooxxooxx
xoooxxooxx
xxooooooxx
xxxxooooxx
xxxxxoooxx
xxoooxxxxx
xxoooxxxxx

Row1 -> 0111001100
Row2 -> 0122001200


xx000xx
xxxxxxx


0011100
0000000


011
012

If m traversing row wise for every i, j separate matrix -> largest square seen so for and i, j == x then M[i][j] = 0
If h > w
	Make a square of w, w
If w > h
	Make a square of h, h
If w == h
	Make the entire component a square.

Given a board with some spaces open ("o"s), place a bunch of squares on the board to cover
all the "o"s and none of the "x"s. Try to minimize the number of squares (not a hard requirement).

def traverse(grid):
	M = len(grid) #height
	N = len(grid[0]) #width

	S = [[0 for i in range(N)] for j in range(M)]
	I, J = 0, 0
	for I in range(M):
		for J in range(N):
			if grid[I][J] == ‘x’:
				S[I][J] = 0
			elif: I == 0 or J == 0:
				S[I][J] = 1
            else:
	            S[I][J] = min(S[I-1][J], S[I][J-1], S[I-1][J-1])+1



    Count = 0
	for I in range(M):
		for J in range(N):
            Part1 = S[I+1][J] if I + 1 < M else -sys.maxint
            Part2 = S[I][J+1] if J + 1 < N else -sys.maxint
            Part3 = S[I+1][J+1] if I + 1< M and J + 1 < N else -sys.maxint

			if S[I][J] >= max(Part1, Part2, Part3):
				count = count + 1
			else:
				continue
return count


"""

