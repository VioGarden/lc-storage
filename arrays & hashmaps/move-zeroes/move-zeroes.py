# use quick sort (swapping values)

def moveZeroes(nums):

    l = 0 # initialize left pointer at 0
    for r in range(len(nums)): # loop over/iterate over array
        if nums[r]: # if the number is not zero
            nums[l], nums[r] = nums[r], nums[l] # swap values of pointers
            # if no zeroes, l and r thre same
            l += 1
            # increment l by 1
    return nums