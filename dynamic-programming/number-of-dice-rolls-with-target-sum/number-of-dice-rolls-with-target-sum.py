def numRollsToTarget(n, k, target):
    """
    :type n: int
    :type k: int
    :type target: int
    :rtype: int
    """
    cache = {}
    def dp(number_of_dice, goal):
        if (number_of_dice, goal) in cache:
            return cache[(number_of_dice, goal)]
        if (number_of_dice == 0):
            return 1 if goal == 0 else 0
        curr_count = 0
        for scenario in range(max(0, goal-k), goal):
            curr_count += dp(number_of_dice - 1, scenario)
        cache[(number_of_dice, goal)] = curr_count
        return curr_count
    return dp(n, target) % (10**9 + 7)