def minFlipsMonoIncr(s):
    min_flips = flips = s.count('0')
    for c in s:
        if c == '1':
            flips += 1
        else:
            flips -= 1
            min_flips = min(min_flips, flips)
    return min_flips