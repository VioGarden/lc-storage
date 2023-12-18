def numSubseq(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    final = 0
    while left <= right:
        if nums[left] + nums[right] > target:
            right -= 1
        else:
            final += pow(2, right - left, 10**9+7)
            left += 1
    return final % (10**9 + 7)
        

print(numSubseq([3,5,6,2], 9)) # 12
print(numSubseq([3,3,6,8], 10)) # 6
print(numSubseq([2,3,3,4,6,7], 12)) # 61

