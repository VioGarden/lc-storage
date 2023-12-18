def findDuplicate(nums):
    for i in range(len(nums)):
        curr = nums[i]
        curr = abs(curr)
        if nums[curr] < 0:
            return curr
        nums[curr] = -nums[curr]
    return nums[0]