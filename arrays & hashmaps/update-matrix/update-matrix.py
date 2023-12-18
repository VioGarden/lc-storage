def updateMatrix(mat):

    ROWS, COLS = len(mat), len(mat[0])

    queue = []

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for r in range(ROWS):
        for c in range(COLS):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = "*"

    for r, c in queue:
        for dr, dc in directions:
            row = r + dr
            col = c + dc
            if 0 <= row < ROWS and 0 <= col < COLS and mat[row][col] == "*":
                mat[row][col] = mat[r][c] + 1
                queue.append((row, col))

    return mat
