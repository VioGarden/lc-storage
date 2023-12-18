# n = n & (n-1) then result += 1
# n = n & (n-1) <-- gets rid of a bit

def hammingWeight(n):
    res = 0 
    while n: # while n
        n &= (n-1) # shortcut, subtracts 1 from bit each time
        res += 1
    return res