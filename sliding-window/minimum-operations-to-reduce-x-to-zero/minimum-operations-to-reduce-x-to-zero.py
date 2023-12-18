def minOperations(nums, x):
    """
    :type nums: List[int]
    :type x: int
    :rtype: int
    """
    n = len(nums)
    left = right = 0
    ans = float('inf')
    current_sum = 0
    target = sum(nums) - x
    while right < n:
        current_sum += nums[right]
        right += 1
        while current_sum > target and left < right:
            current_sum -= nums[left]
            left += 1
        if current_sum == target:
            ans = min(ans, n - (right - left))
    return -1 if ans == float('inf') else ans