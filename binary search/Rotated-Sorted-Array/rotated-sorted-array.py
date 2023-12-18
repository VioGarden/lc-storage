def search(nums, target):
    left, right = 0, len(nums) - 1 # initialize pointers to edges 
    while left <= right: # while pointers do not cross
        mid = (left + right)//2 # mid index
        if target == nums[mid]: # if mid is answer, return the index
            return mid 
        if nums[left] <= nums[mid]: # left sorted portion
            # if target is greater than mid value or target is less than left most value
            if target > nums[mid] or target < nums[left]: 
                left = mid + 1 # left pointer + 1
            else: # if target is in range between left pointer and mid
                right = mid - 1 # right pointer - 1
        else: # right sorted position
            # if target is less than mid, or greater than right most value
            if target < nums[mid] or target > nums[right]:
                right = mid - 1 # right pointer - 1
            else: # if target is in range of mid and right most value
                left = mid + 1 # left + 1
    return -1 # nothing found, return -1

print(search([4,5,6,7,0,1,2], 6))