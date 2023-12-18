# memoized
def countGoodString(low, high, zero, one):
    mod = 10**9 + 7
    dp = {}

    def helper(length):
        if length > high:
            return 0
        if length in dp:
            return dp[length]
        dp[length] = 1 if length >= low else 0
        dp[length] += helper(length + zero) + helper(length + one)
        return dp[length] % mod
    return helper(0) 