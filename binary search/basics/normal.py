def binn(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


x = [1,2,3,4,6,7,8,9]
print(binn(x, 4))        
print(binn(x, 5))        
