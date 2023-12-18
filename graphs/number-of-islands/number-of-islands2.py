def numIslands(grid):

    rows, cols = len(grid), len(grid[0])

    visited = set()

    count = 0

    def helper(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return
        grid[r][c] = "*"
        helper(r + 1, c)
        helper(r - 1, c)
        helper(r, c + 1)
        helper(r, c - 1)


    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and grid[i][j] == "1":
                helper(i, j)
                count += 1
    
    return count