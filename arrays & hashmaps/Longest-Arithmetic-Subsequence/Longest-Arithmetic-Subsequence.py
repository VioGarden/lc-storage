def longestSubsequence(arr, difference):
    dp = {}
    for x in arr:
        if x - difference in dp:
            dp[x] = dp[x - difference] + 1
        else:
            dp[x] = 1
    return max(dp.values())

print(longestSubsequence([1,2,3,4], 1))