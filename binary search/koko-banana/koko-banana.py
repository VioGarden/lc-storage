import math

def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    res = right

    while left <= right:
        k = (1 + right)//2
        hours = 0
        for i in piles:
            hours += math.ceil(i/k)
        if hours <= h:
            res = min(res, k)
            right = k - 1
        else:
            left = k + 1
    return res

print(minEatingSpeed([3,6,7,11], 8))
print('hi')
