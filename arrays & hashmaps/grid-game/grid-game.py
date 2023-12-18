def gridGame(grid):
    if len(grid[0]) != len(grid[1]):
        return 0

    pref = [0]*len(grid[0])
    prefsum = 0
    suff = [0]*len(grid[1])
    suffsum = 0

    for i in range(len(grid[1])):
        pref[i] = prefsum
        prefsum += grid[1][i]

    for j in range(len(grid[0])-1, -1, -1):
        suff[j] = suffsum
        suffsum += grid[0][j]

    print(pref, suff)
    low = float("inf")
    for i in range(len(grid[0])):
        low = min(max(pref[i], suff[i]), low)
    
    return low

grid = [[1,3,1,15],[1,3,3,1]]
gridGame(grid)