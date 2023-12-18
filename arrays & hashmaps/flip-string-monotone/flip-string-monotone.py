# finding dividing place in s

def minFlipsMonoIncr(s):
    # step 1: find number of zeroes
    # min_flips = flips = s.count('0') // shorter more concise way
    zero_count = 0
    for bite in s:
        if bite == '0':
            zero_count += 1
    
    min_flips = zero_count # two different variables count zero
    flips = zero_count # flips makes more sense as a name
    
    # iterate over byte string again
    for char in s:
        # if the character is 1, increment flips by one
        if char == '1':
            flips += 1
        # if character is 0, decrement flips by one and check if it is the lowest
        else:
            flips -= 1
            min_flips = min(flips, min_flips)
    return min_flips

