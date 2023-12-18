def countNegatives(grid):
    ans = 0
    ending = len(grid[0])
    row, col = len(grid), len(grid[0])
    for i in range(len(grid)):
        for j in range(ending):
            if grid[i][j] >= 0:
                continue
            else:
                ending = j
                break
        ans += col - ending
    return ans