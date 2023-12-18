def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            x = nums[i] + nums[left] + nums[right]
            if x == target:
                return x
            if abs(x - target) < abs(result - target):
                result = x
            if x > target:
                right -= 1
            else:
                left += 1
    return result
