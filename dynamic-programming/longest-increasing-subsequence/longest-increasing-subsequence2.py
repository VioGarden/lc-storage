def lengthOfLIS(nums):
    arr = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                arr[i] = max(arr[i], 1 + arr[j])
    return max(arr)