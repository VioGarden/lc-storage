# xor

def singleNumber(nums):
    res = 0 # result 
    for n in nums: # iterating over nums array
        res = n ^ res # xor value, if two are identical, cancels out
    return res # single value that doesn't get xor