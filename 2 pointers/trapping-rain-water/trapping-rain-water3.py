def trap(height):
    left, right, minlr = [0], [0], [] # initialize left and right and min
    val = 0 # value of min
    # normally, len(height) does work, but because 0 already, -1
    for i in range(len(height)-1): # range(a,b,c)
        # val to append is max left value
        val = max(height[i], val)
        left.append(val) # append to left list
    val = 0
    # len(height) <-- iteration error because starting from the back
    for j in range(len(height)-1, 0, -1): # 0 will not count in iteration
        # val is max as you are iterating
        val = max(height[j], val)
        # append to list
        right.append(val)
    # reverse because then in matches original meaning of iterating from back
    right.reverse()
    # for length of the lists
    for k in range(len(right)):
        # append the minimum of both values, lowest where you can trap water
        minlr.append(min(left[k], right[k])) # correct list being called
    # total trapable water count
    rain_trap = 0
    # for range
    for l in range(len(minlr)):
        # if possible boundaries are higher than spaces
        if minlr[l] > height[l]:
            # difference is added to count
            rain_trap += (minlr[l] - height[l])
    return rain_trap

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    
