def findMin(nums):
    result = nums[0] # can be anything
    left, right = 0, len(nums) - 1 # initialize pointers to ends

    while left <= right: # while left is less than right
        if nums[left] < nums[right]: # if the array every becomes one, know min is at the left
            result = min(result, nums[left]) # find min and store to result
            break # break out of while loop
        mid = (left + right)//2 # binary search conitinues
        result = min(result, nums[mid]) # result is the lower of former result and mid value
        if nums[mid] >= nums[left]:  # if value at mid is greater than left value, know on left side and can move left pointer
            left = mid + 1
        else:
            right = mid - 1 # else, know on right side and can move right pointer
    return result


findMin([3,4,5,1,2])