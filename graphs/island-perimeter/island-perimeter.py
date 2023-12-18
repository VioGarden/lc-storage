def islandPerimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    def check_sides(row, col):
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return 1
        if grid[row][col] == 0:
            return 1
        return 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue
            perimeter += check_sides(r + 1, c)
            perimeter += check_sides(r - 1, c)
            perimeter += check_sides(r, c + 1)
            perimeter += check_sides(r, c - 1)
    return perimeter