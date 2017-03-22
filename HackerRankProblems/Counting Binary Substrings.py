
import sys
def count(s):
    n=len(s)
    matrix=[ [0 for _ in range(n)] for _ in range(n)]

    newS=[]
    print matrix

    for item in s:
        if (item =='0'):
            newS.append(1)
        else:
            newS.append(-1)

    print newS, newS[1]
    result=0
    for i in range(n):
        for j in range(n):
            #print i, j
            if (i == j):
                matrix[i][i]=newS[j]
            elif(j > i):
                matrix[i][j]=matrix[i][j-1] + newS[j]
                if (matrix[i][j] == 0):
                    result = result + 1

    print matrix, result

if __name__=="__main__":
    s="00110"
    print count(s)