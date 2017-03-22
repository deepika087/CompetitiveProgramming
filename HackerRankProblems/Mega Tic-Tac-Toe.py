

def anyHorizontal(matrix, n, m, k, character):

    for i in range(n):
        data=matrix[i]
        target=character*k
        #print "target", target
        if (target in data):
            return True
    return False

def anyVertical(matrix, n, m, k, character):
    target=character*k
    for i in range(m):
        data=[]
        for j in range(n):
            data.append(matrix[j][i])
        if (target in ''.join(data)):
            return True
    return False

def anyDiagonal(matrix, n, m, k, character):
    if (n!=m):
        return False
    target=character*k
    data=[]
    for i in range(n):
        for j in range(m):
            if (i == j):
                data.append(matrix[i][i])
    if (target in ''.join(data)):
        return True
    return False

    data=[]
    for i in range(n):
        for j in range(m):
            if (i + j == (n-1)):
                data.append(matrix[i][i])
    if (target in ''.join(data)):
        return True
    return False

def whowon(matrix, n, m, k):
    alex=False
    otherPlayer=False

    alex = anyHorizontal(matrix, n, m, k, 'O') or anyVertical(matrix, n, m, k, 'O') or anyDiagonal(matrix, n, m, k, 'O')
    otherPlayer = anyHorizontal(matrix, n, m, k, 'X') or anyVertical(matrix, n, m, k, 'X') or anyDiagonal(matrix, n, m, k, 'X')

    if ( alex and not otherPlayer):
        return "WIN"
    elif( not alex and otherPlayer):
        return "LOSE"
    else:
        return "NONE"


if __name__=="__main__":
    g=int(raw_input(''))
    for i in range(g):
        nmk=raw_input('')
        nmk=nmk.split()
        (n,m,k)=(int(nmk[0]), int(nmk[1]), int(nmk[2]))
        matrix=[]
        for j in range(n):
            matrix.append(raw_input())
        print whowon(matrix, n, m, k)

