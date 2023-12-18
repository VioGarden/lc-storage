def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1: return 0 # if obstacleGrid is empty or top left is obstacled, return 0

    dp = [0] * len(obstacleGrid[0])

    dp[0] = 1

    for r in range(len(obstacleGrid)):
        for c in range(len(obstacleGrid[0])):

            if obstacleGrid[r][c] == 1: # if current square is blocked
                dp[c] = 0 # cut off funding

            elif c > 0:  # if col number is greater
                dp[c] += dp[c - 1] # increase by prev
    
    return dp[-1]