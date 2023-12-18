def longestOnes(nums, k):
    n, ans, left = len(nums), 0, 0
    for right in range(n):
        if nums[right] == 0:
            if k == 0:
                while nums[left] != 0:
                    left += 1
                left += 1
            else:
                k -= 1
        ans = max(ans, right - left + 1)
    return ans