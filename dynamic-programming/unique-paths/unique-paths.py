def uniquePaths(m, n):
    rows, cols = m, n
    dp = [[1 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[rows-1][cols-1]


import math

def uniquePaths(m, n):
    return int(math.factorial(m + n - 2)/(math.factorial(m - 1)*math.factorial(n - 1)))


def uniquePaths(m, n):
    # m + n - 2 (n)
    # m - 1 or n - 1 (k)

    # C(n, k)

    # n!/k!*(k - n)!

    # (m + n - 2)!/(m - 1)!(n - 1)!

    total, mm, nn = 1, 1, 1

    for i in range(1, m + n - 1):
        total *= i
    
    for j in range(1, m):
        mm *= j

    for k in range(1, n):
        nn *= k
    
    return total//(mm*nn)