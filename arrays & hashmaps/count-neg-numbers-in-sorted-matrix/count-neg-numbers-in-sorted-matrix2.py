def countNegatives(grid):
    m, n = len(grid), len(grid[0])
    row, col, ans = 0, n - 1, 0
    while row < m and col >= 0:
        if grid[row][col] < 0:
            ans += m - row
            col -= 1
        else:
            row += 1
    return ans