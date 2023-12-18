def stoneGame(piles):
    n = len(piles)
    array = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        array[i][i] = piles[i]
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            array[i][j] = max(piles[i] - array[i + 1][j], piles[j] - array[i][j - 1])
    
    return array[0][n - 1] > 0