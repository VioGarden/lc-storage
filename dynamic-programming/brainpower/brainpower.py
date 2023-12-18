# recursive with memoization
def mostPoints(questions):

    # Time (n)
    # Time (n)

    dp = {} # memoize

    def helper(i):
        if i >= len(questions): # if i is out of bounds
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max(
            helper(i + 1),# skip question
            questions[i][0] + helper(i + 1 + questions[i][1]) # solve curr question
        )
        return dp[i]
    return helper(0)
