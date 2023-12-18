def minPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    n = len(nums)
    left, right = 0, n - 1
    ans = nums[left] + nums[right]
    while left < right:
        left += 1
        right -= 1
        ans = max(ans, nums[left] + nums[right])
    return ans