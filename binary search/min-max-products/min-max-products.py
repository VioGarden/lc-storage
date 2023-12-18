def minimizedMaximum(n, quantities):
    left, right = 1, max(quantities)
    # as soon as left crosses right, end the while loop
    while left < right:
        mid = (left + right)//2
        tot = 0
        # tot will sum of ceil with mid
        for j in quantities:
            var = -(-j//mid) 
            tot += var
        # if tot is greater, means mid is too small
        if tot > n:
            left = mid + 1
        # if tot is less, means mid is too big
        else:
            right = mid
    return left