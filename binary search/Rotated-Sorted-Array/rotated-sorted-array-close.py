def search(nums, target):
    left, right = 0, len(nums) - 1 # initialize left and right pointers
    while left <= right:
        mid = (left + right)//2 # index of mid
        mid_val = nums[mid] # value of mid
        if target == mid_val: # moved these two lines here to shorten code
            return mid # if mid is value, return mid, answer
        # if value of mid is greater than left most value pointer
        if mid_val >= nums[left]: # mid_val > nums[left] --> mid)val >= nums[left] **forgot >=
            # if target == mid_val: >>> return mid # code was originally here and in next case
            if target >= nums[left] and target < mid_val: # if target is in range of left most and mid
                right = mid - 1 # right pointer gets decreased
            else: # if not in range
                left = mid + 1 # left pointer increased
        else: # value if mid is not greater than left most, checking right side
            # if target == mid_val: >>> return mid
            if target > mid_val and target <= nums[right]: # if in range of right edge value and mid value
                left = mid + 1 # left pointer gets shifted
            else: # if not in range 
                right = mid - 1 # right pointer shifted
    return -1 # return -1 if nothing found

# works for big cases, not small cases

print(search([4,5,6,7,0,1,2], 6))