
def plusOne(digits):
    digits = digits[::-1] # reversing array
    # one is the carry
    # i is the index of position
    one, i = 1, 0

    while one: # while one == 1
        if i < len(digits): # i is inbounds
            if digits[i] == 9: # when digit 9
                # one = 1 # carry still exists
                digits[i] = 0 # turn into one
            else: # when digits is not 9
                digits[i] += 1 # increment by one
                one = 0 # carry is gone
        else: # i is out of bounds
            digits.append(1) # carry
            one = 0 # then set carry to zero
        i += 1 # next index of number
    return digits[::-1] # reverse the reversed array