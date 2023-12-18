def shortestBridge(grid):

    n = len(grid)

    def dfs(i, j):
        grid[i][j] = -1
        bfs.append((i, j))
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                dfs(x, y)
    
    def first():
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    return i, j
    
    step = 0
    bfs = []

    dfs(*first())

    while bfs:
        new = []
        for i, j in bfs:
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        return step
                    elif not grid[x][y]:
                        grid[x][y] = -1
                        new.append((x, y))
        
        step += 1
        bfs = new
        
        