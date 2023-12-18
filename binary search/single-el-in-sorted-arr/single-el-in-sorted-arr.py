def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right)//2
        if mid % 2 == 1: # gets to even index 
            mid -= 1
        if nums[mid] != nums[mid + 1]:
            right = mid
        else:
            left = mid + 2
    return nums[left]

# [3,3,7,7,10,11,11,12,12,15,16]