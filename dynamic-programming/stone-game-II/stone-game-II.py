def stoneGameII(piles):

    dp = {}
    def helper(alice, i, m):
        if i == len(piles):
            return 0
        if (alice, i, m) in dp:
            return dp[(alice, i,  m)]
        
        res = 0 if alice else float("inf")
        total = 0
        for x in range(1, 2*m + 1):
            if i + x > len(piles):
                break
            total += piles[i + x - 1]
            if alice:
                res = max(res, total + helper(not alice, i + x, max(m, x)))
            else:
                res = min(res, helper(not alice, i + x, max(m,x)))
        dp[(alice, i, m)] = res
        return res
    return helper(True, 0, 1)
