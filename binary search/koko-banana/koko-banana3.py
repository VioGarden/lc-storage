import math

def minEatingSpeed(piles, h):
    most = 0
    for i in piles:
        if i > most:
            most = i
    left, right = 1, most
    final = most
    while left <= right:
        mid = (left + right)//2
        curr = 0
        for j in piles:
            c = math.ceil(j/mid)
            curr += c
        if curr <= h:
            final = mid
            right = mid - 1
        else:
            left = mid + 1
    return final