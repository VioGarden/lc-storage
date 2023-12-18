def threeSum(nums):
    res = [] # result list
    nums.sort() # sort the nums (n log n time)

    # first value in three sum will be i   (not left or right)
    for i, a in enumerate(nums): # index, value of nums
        if i > 0 and a == nums[i-1]: # if index isn't first and value of a is before
            continue # next iteration

        # left is second value (i + 1), right is third value (end of list)
        left, right = i + 1, len(nums) - 1 
        # run while left is less than right, if they cross, next iteration of for loop
        while left < right:
            # a (value of i) + value of left + value of right
            threeSum = a + nums[left] + nums[right] 
            # if threeSum overshoots zero, decrease threeSum by decrementing right
            if threeSum > 0: 
                right -= 1
            # if threeSum undershoots zero, increase threeSum by incrementing left
            elif threeSum < 0:
                left += 1
            # if threeSum equals zero, add to list
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                # now searching for more matches for i
                # while left shift equals previous, and left is still less than right
                while nums[left] == nums[left - 1] and left < right:
                    # increment left by one
                    left += 1
    return res
print(threeSum([-1,0,1,2,-1,-4]))