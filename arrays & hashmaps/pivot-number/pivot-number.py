def pivotIndex(nums):
    left = 0 
    right = sum(nums) # total sum
    for i, v in enumerate(nums):
        right -= v # subtrack value from total sum
        if left == right: # if the same, return index
            return i
        left += v # add to left
    return -1
        