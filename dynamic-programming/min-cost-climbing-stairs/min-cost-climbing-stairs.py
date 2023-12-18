def minCostClimbingStairs(cost):
    first, second = cost[0], cost[1]
    for i in range(2, len(cost)):
        temp = cost[i] + min(first, second)
        first, second = second, temp
    return min(first, second)
