def findDuplicate(nums):
    while nums[0] != nums[nums[0]]:
        nums[nums[0]], nums[0]  =  nums[0], nums[nums[0]]
        #nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
    return nums[0]