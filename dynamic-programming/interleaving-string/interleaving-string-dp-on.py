def isInterleave(s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    dp = [True for _ in range(c+1)] 
    for j in range(1, c+1):
        dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
    for i in range(1, r+1):
        dp[0] = (dp[0] and s1[i-1] == s3[i-1])
        for j in range(1, c+1):
            dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
    return dp[-1]

ss1 = "aabcc"
ss2 = "dbbca"
ss3 = "aadbbcbcac"

print(isInterleave(ss1, ss2, ss3))