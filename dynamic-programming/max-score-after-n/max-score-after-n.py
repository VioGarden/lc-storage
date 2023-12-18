# use bitmask
from collections import defaultdict
def maxScore(nums):
    cache = defaultdict(int)
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return abs(a)
        
    def helper(mask, op):
        if mask in cache:
            return cache[mask]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (1 << i) & mask or (1 << j) & mask:
                    continue
                newMask = mask | (1 << i) | (1 << j)
                score = op * gcd(nums[i], nums[j])
                cache[mask] = max(
                    cache[mask],
                    score + helper(newMask, op + 1)
                )
        return cache[mask]
    return helper(0, 1)