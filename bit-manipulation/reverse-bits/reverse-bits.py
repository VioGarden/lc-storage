def reverseBits(n):
    res = 0
    for i in range(32): # 32 bit go thru every bit
        bit = (n >> i) & 1 # ith bit of n (n is target bit in 1 spot)
        # logic or with output ( i goes from 0 --> 31)
        res = res | (bit << (31-i)) # shift bit by (31-i)
    return res

