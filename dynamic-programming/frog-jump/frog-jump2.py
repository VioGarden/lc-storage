def canCross(stones):
    dp = [set() for _ in range(len(stones))]

    dp[0].add(1)

    for i in range(1, len(stones)):
        for j in range(i):
            difference = stones[i] - stones[j]
            if difference in dp[j]:
                dp[i].add(difference + 1)
                dp[i].add(difference)
                dp[i].add(difference - 1)
    
    return True if len(dp[-1]) > 0 else False
