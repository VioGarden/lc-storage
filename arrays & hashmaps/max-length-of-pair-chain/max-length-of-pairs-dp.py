def findLongestChain(pairs):
    n = len(pairs)
    pairs.sort(key = lambda x: x[1])
    dp = [1] * n

    for i in range(1, n):
        dp[i] = max(dp[i], max(dp[j] + 1 if pairs[i][0] > pairs[j][1] else 1 for j in range(i)))

    return max(dp)
    