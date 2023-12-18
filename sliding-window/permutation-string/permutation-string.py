def checkInclusion(s1, s2):
    if len(s1) > len(s2): # edge case, if s1 is longer 
        return False # no permutations possible

    s1_count, s2_count = [0] * 26, [0] * 26 # implement arrays, fixed values, indeces of array
    for i in range(len(s1)): # go through every character in s1
        s1_count[ord(s1[i]) - ord('a')] += 1 # updating array (array of 1 and 0)
        s2_count[ord(s2[i]) - ord('a')] += 1 # updating array (array of 1 and 0)

    matches = 0 # matches
    for i in range(26): # loop through array
        # to matches, add 1 if the count at index are equal
        matches += 1 if s1_count[i] == s2_count[i] else 0

    l = 0 # sliding window portion
    for r in range(len(s1), len(s2)): # every position at s2 (start at length of s1)
        if matches == 26: # if matches is 26 (everything matches)
            return True # return immediately

        index = ord(s2[r]) - ord('a') # get index of count array
        # index is character that was just added
        s2_count[index] += 1 # increment that index by one
        # if incrementing the s2 index makes the thing match to the s1 array
        if s1_count[index] == s2_count[index]: 
            matches += 1 # increment matches
        # if incrementing the s2 index makes the thing dematch not match the s1 array
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1 # decrement matches
        
        # do opposite for index l
        index = ord(s2[l]) - ord('a')
        # below is character we just removed
        s2_count[index] -= 1
        # if by decrementing, by decrementing, made it equal
        if s1_count[index] == s2_count[index]:
            matches += 1 # +1 to matches
        # if by decrementing, make it less of a match
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1 # -1 to matches
        l += 1 # increment left by 1
    # last case, for final letters (because check happens before)
    return matches == 26 # True or False

