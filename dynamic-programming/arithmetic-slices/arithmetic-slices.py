def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    curr_diff, count, ans = -1, 0, 0
    for i in range(1, len(nums)):
        new_diff = nums[i] - nums[i - 1]
        if curr_diff != new_diff:
            curr_diff, count = new_diff, 1
        else:
            ans += count
            count += 1
    return ans
