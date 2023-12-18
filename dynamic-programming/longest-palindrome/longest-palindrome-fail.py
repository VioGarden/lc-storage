def longestPalindrome(s):
    sss = list(s)
    longest = []
    for i in range(len(sss)):
        left, right = i, i
        if left - 1 >= 0 and sss[left - 1] == sss[i]:
            left -= 1
        if right + 1 < len(s) and sss[right + 1] == sss[i]:
            right += 1
        while left - 1 >= 0 and right + 1 < len(sss) and sss[left - 1] == sss[right + 1]:
            left, right = left - 1, right + 1
        if i > 0 and left == right:
            continue
        longs = len(longest)
        if left == 0 and right == len(sss) - 1:
            if len(sss[:]) > longs:
                longest = sss[:]
        elif left == 0:
            if len(sss[:right+1]) > longs:
                longest = sss[:right+1]
        elif right == len(s) - 1:
            if len(sss[left-1:]) > longs:
                longest = sss[left-1:]
        else:
            if len(sss[left:right+1]) > longs:
                longest = sss[left:right+1]
    x = "".join(longest)
    return x

# failed code

# errors
# , instead of : when indexing
# **ordering in --> if ... and ... statements matter
# indexing incorrectly


longestPalindrome("babad")