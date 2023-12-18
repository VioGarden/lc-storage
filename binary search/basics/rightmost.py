def binr(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = -((-left - right)//2)
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    return right

x = [0,1,2,3,3,3,3,3,3,3,3,4,5,6]
print(binr(x, 3))