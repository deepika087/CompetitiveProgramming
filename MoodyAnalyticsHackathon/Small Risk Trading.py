

if __name__=="__main__":
    NK = raw_input('')
    NK = NK.split()
    N = int(NK[0])
    K = int(NK[1])

    matrix = []
    for i in range(0,3):
        line = raw_input('')
        line = line.split()
        matrix.append(line)
    #print(matrix)
    #print matrix[1][0]

    result = []
    for i in range(0, N): # Data for N days but kept column wise
        a = float(matrix[0][i]) * float(matrix[1][i])
        b = float( 1 - float(matrix[0][i])) * float(matrix[2][i])
        result.append( float ( a - b))

    result = sorted(result, reverse=True)
    #print result
    sum = 0.0
    for i in range(0, K):
        if (result[i] + sum < sum):
            break
        sum = sum + result[i]

    print("{0:.2f}".format(round(sum,2)))

