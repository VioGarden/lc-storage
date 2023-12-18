def setZeroes(matrix):
    # extra sets
    # O(m*n)
    rowset = set()
    colset = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rowset.add(i)
                colset.add(j)
    for k in range(len(matrix)):
        for j in range(len(matrix[0])):
            if k in rowset or j in colset:
                matrix[k][j] = 0
    return
    