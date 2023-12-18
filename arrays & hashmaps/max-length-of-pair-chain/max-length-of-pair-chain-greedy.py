def findLongestChain(pairs):
    n = len(pairs)
    pairs.sort(key = lambda x: x[1])
    ans = 0
    cur = -1001
    for head, tail in pairs:
        if head > cur:
            cur = tail
            ans += 1
    return ans