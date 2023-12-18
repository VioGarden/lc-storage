def rotate(matrix):
    mlist = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)-1, -1, -1):
            mlist.append(matrix[j][i])

    
    p = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = mlist[p]
            p += 1