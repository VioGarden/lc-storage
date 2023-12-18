def generate(numRows):
    ans = [[1] * (n) for n in range(1, numRows + 1)]
    for i in range(numRows):
        for j in range(1, i):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
    return ans