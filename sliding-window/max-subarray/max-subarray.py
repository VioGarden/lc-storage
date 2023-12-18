def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    
    count = nums[0]
    curr = 0
    for n in nums:
        if curr < 0:
            curr = 0
        curr += n
        count = max(count, curr)
    return count
            