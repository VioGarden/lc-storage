def lengthOfLongestSubstring(s):
    charSet = set() # set of non duplicates
    left = 0 # initialize left pointer
    res = 0 # result of length of longest string
    for r in range(len(s)): # use for loop for right side of sliding window
        while s[r] in charSet: # while loop, to remove duplicate and pre cursors
            charSet.remove(s[left]) # left pointer only moves if duplicates
            left += 1 # shifting left pointer over 
        charSet.add(s[r]) # add the right most value in string to charset
        res = max(res, r - left + 1) # each iteration, keep track of longest length
    return res # return longest length
    

        

        


# two pointer sliding window problem
# when find repeated value, remov e from the start
# use a set
