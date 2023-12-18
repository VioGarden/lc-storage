def minPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_val = min_val = ans = 0
    bucket = [0] * 100001

    for i in nums:
        bucket[i] += 1
        max_val = max(max_val, i)
        min_val = min(min_val, i)
    
    left, right = min_val, max_val
    
    while left <= right:
        if bucket[left] == 0:
            left += 1
        elif bucket[right] == 0:
            right -= 1
        else:
            ans = max(ans, left + right)
            bucket[left] -= 1
            bucket[right] -= 1
    return ans