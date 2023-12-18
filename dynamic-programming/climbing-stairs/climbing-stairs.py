# bottom up dynamic programming
# base case, memoization
# https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=5s&ab_channel=NeetCode

def climbStairs(n):
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one
        