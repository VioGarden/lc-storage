def stoneGame(piles):
    n = len(piles)
    f = [0] * n
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            f[j] = max(piles[i] - f[j], piles[j] - f[j - 1])
    
    return f[n - 1] > 0