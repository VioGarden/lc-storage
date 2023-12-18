def longestPalindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)): # each i in s
        # odd length palindromes
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]: 
            # l >= 0 and r < len(s) <-- in bounds
            # s[l] == s[r] <-- condition to continue
            if (r - l + 1) > resLen: # (r - l + 1) or (r + 1 - l) <-- length of substring
                res = s[l: r + 1] # works because still inbounds
                resLen = (r - l + 1) # update length of substring
            l -= 1 # change left pointer
            r += 1 # change right pointer
        # even length palindromes
        l, r, = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = (r - l + 1)
            l -= 1
            r += 1
    return res
    # if statements inside while


        