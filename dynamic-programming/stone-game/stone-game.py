def stoneGame(piles):
    
    def helper(piles, l, r, cache):
        if (l, r) in cache:
            return cache[(l, r)]
        if l > r:
            return 0
        if l == r:
            return piles[l]
        res = max(piles[l] - helper(piles, l + 1, r, cache), piles[r] - helper(piles, l, r - 1, cache))
        cache[(l, r)] = res
        return res

    return helper(piles, 0, len(piles) - 1, {}) > 0