def minTaps(n, ranges):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for index, value in enumerate(ranges):
        start, end = max(0, index - value), min(n, index + value)
        for j in range(start, end + 1): # (start, end + 1) works as well
            dp[j] = min(dp[j], dp[start] + 1)
    
    return -1 if dp[-1] == float('inf') else dp[-1]