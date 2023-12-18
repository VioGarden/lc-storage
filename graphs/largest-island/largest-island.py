
def maxAreaOfIsland(self, grid):
    rows, cols = len(grid), len(grid[0])
    visit = set()

    def dfs(r,c):
        if (r < 0 or # out of bounds
            r == rows or  # out of bounds
            c < 0 or  # out of bounds
            c == cols or  # out of bounds
            grid[r][c] == 0 or # if water block
            (r,c) in visit): # if already in visit hash set
            return 0
        
        # on valid square
        visit.add((r,c)) # add to hash set
        # returns a number (1 is init island)
        return (1 + dfs(r+1, c) + # checking neighbor
                    dfs(r-1, c) + # checking neighbor
                    dfs(r, c + 1) + # checking neighbor
                    dfs(r, c - 1)) # checking neighbor

    area = 0 # init area = 0
    for r in range(rows): # iterating over whole grid
        for c in range(cols):
            area = max(area, dfs(r, c)) # biggest island set to area

    return area 