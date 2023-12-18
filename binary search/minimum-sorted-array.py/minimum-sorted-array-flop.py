def findMin(nums):
    left, right = 0, len(nums) - 1
    while nums[left] > nums[right]:
        mid = (left + right)//2
        midVal = nums[mid]
        if mid >= left:
            left = mid
        else:
            right = mid
            
    return nums[left]

findMin([3,4,5,1,2])