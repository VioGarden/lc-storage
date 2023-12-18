def binl(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right)//2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


x = [0,1,2,3,3,3,3,3,3,3,4,5,6]
print(binl(x, 3))




