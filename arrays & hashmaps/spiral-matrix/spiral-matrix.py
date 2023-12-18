class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        output = []
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        counter = 0

        def right(i, j):
            while (j+1) < n and matrix[i][j+1] != -101:
                output.append(matrix[i][j])
                matrix[i][j] = -101
                j += 1
            return (i, j)
        
        def left(i, j):
            while (j-1) >= 0 and matrix[i][j-1] != -101:
                output.append(matrix[i][j])
                matrix[i][j] = -101
                j -= 1
            return (i, j)

        def up(i, j):
            while (i - 1) >= 0 and matrix[i-1][j] != -101:
                output.append(matrix[i][j])
                matrix[i][j] = -101
                i -= 1
            return (i, j)

        def down(i, j):
            while (i + 1) < m and matrix[i+1][j] != -101:
                output.append(matrix[i][j])
                matrix[i][j] = -101
                i += 1
            return (i, j)

        cachei, cachej = -102, -102
        while matrix[i][j] != -101:
            if counter == 0:
                i, j = right(i, j)
            elif counter == 1:
                i, j = down(i, j)
            elif counter == 2:
                i, j = left(i, j)
            else:
                i, j = up(i, j)
            if cachei == i and cachej == j:
                output.append(matrix[i][j])
                break
            cachei, cachej = i, j
            counter = (counter + 1) % 4
        return output