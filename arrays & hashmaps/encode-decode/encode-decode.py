def encode(strs):
    output = ""                   #initialize output
    for i in strs:                #loop over strs
        output += str(len(i)) + "#" + i     #concatinate to string
    return output                 #return output

def decode(strs):
    output, i = [], 0             #initialize output, initialize index iterator variable

    while i < len(strs):          #will run until no more str (cant do for because dont know number of iterations)
        j = i                     #j is a temporary variable (not permanent)
        while strs[j] != "#":     #quick while loop to get length
            j += 1                #when get "#", break out know length of length number (single, double digits)
        length = int(strs[i:j])   #length starts at i, ends at #, so this works
        output.append(strs[j + 1 : j + 1 + length])   #append to list, (+1 because of #)
        i = j + 1 + length        #set i to end of first word, length + # + element
    return output                 #return output
    
decode(encode(["violet", "evergarden", "the", "movie"]))