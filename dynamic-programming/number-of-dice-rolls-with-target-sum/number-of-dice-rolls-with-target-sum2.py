def numRollsToTarget(n, k, target):
    """
    :type n: int
    :type k: int
    :type target: int
    :rtype: int
    """

    dp = [[0] * (n + 1) for _ in range(target + 1)]

    for i in range(1, k + 1):
        if i <= target:
            dp[i][1] = 1
        else:
            break
    
    for b in range(2, n + 1):
        for c in range(b, target + 1):
            dp[c][b] = dp[c - 1][b - 1] + dp[c - 1][b] - dp[c - min(c - 1, k) - 1][b - 1]
    return dp[target][n] % (10**9 + 7)

def numRollsToTarget(n, k, target):
    dp = [[0] * (n + 1) for _ in range(target + 1)]

    for i in range(1, k + 1):
        if i <= target:
            dp[i][1] = 1
        else:
            break
    
    for dice in range(2, n + 1):
        for thing in range(dice, target + 1):
            piece1 = dp[thing - 1][dice - 1]
            piece2 = dp[thing - 1][dice]
            piece3 = dp[thing - min(thing - 1, k) - 1][dice - 1]
            dp[thing][dice] = piece1 + piece2 - piece3
    
    return dp[target][n] % (10**9 + 7)