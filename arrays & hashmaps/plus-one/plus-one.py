def plusOne(digits):
    x = ''.join(str(x) for x in digits) # turn list into string
    y = int(x) + 1 # int of string + 1
    z = str(y) # int back into string
    output = []
    for i in z:
        output.append(i) # turn string back into list
    return output