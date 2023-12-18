class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        return self.helper(text1, text2, 0, 0, memo)

    def helper(self, s1, s2, i, j, memo):
        if memo[i][j] < 0:
            if i == len(s1) or j == len(s2):
                memo[i][j] = 0
            elif s1[i] == s2[j]:
                memo[i][j] = 1 + self.helper(s1, s2, i+1, j+1, memo)
            else:
                memo[i][j] = max(
                    self.helper(s1, s2, i+1, j, memo),
                    self.helper(s1, s2, i, j+1, memo),
                )
        print(memo, i, j, memo[i][j])
        return memo[i][j]

# [[3, -1, -1, -1], [-1, 2, 1, 0], [-1, 2, 1, 0], [-1, -1, 1, 0], [-1, -1, 1, -1], [-1, -1, -1, 0]] 0 0 3