def removeDuplicates(nums):
    ins = 1 # insert indexing value
    for i in range(1, len(nums)): # loop over array except first because sorted and know its first
        if nums[i-1] != nums[i]: # if the current does not match previous
            nums[ins] = nums[i] # the value at index will become next value
            ins += 1 # insert indexing value gets incremented by 1
    return ins # return how many duplicates there are

print(removeDuplicates([1,1,2,2,2,3]))

# [1,2,3,2,2,3] <-- array when looped through