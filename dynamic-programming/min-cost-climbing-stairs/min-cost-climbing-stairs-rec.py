def minCostClimbingStairs(cost):
    def dp(n):
        if n < 2:
            return cost[n]
        return cost[n] + min(dp(n - 1), dp(n - 2))
    return min(dp(len(cost) - 1), dp(len(cost) - 2))