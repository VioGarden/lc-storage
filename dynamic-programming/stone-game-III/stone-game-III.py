# min max
def stoneGameIII(stoneValue):

    cache = {}

    def helper(i):
        if i == len(stoneValue):
            return 0

        if i in cache:
            return cache[i]
        
        res = float("-inf")
        for j in range(i, min(i + 3, len(stoneValue))):
            res = max(res, sum(stoneValue[i:j+1]) - helper(j + 1))
        cache[i] = res
        return res
    
    return "Alice" if helper(0) > 0 else ("Bob" if helper(0) < 0 else "Tie")
