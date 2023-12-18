
def hammingWeight(n): # ez, but must look at every bit
    res = 0 
    while n: 
        res += n % 2 # if res += 1 or 0
        n = n >> 1 # shift bit over by 1
    return res