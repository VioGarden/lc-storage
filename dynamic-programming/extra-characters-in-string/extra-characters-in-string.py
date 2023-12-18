def minExtraChar(s, dictionary):
    highest = len(s) + 1
    dp = [highest] * (len(s) + 1)
    dp[0] = 0
    dictionary_set = set(dictionary)

    for i in range(1, len(s) + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(1, i + 1):
            if s[i - j: i] in dictionary_set:
                dp[i] = min(dp[i], dp[i - j])
    
    return dp[-1]
