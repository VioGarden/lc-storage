def maxFrequency(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()

    ans = curr = left = right = 0

    n = len(nums)

    while right < n:

        curr += nums[right]

        while nums[right] * (right - left + 1) > curr + k:

            curr -= nums[left]
            
            left += 1
        
        ans = max(ans, right - left + 1)

        right += 1

    return ans

nums = [1,4,8,13] 
k = 5
print(maxFrequency(nums, k))