def maximumScore(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ans = nums[k]
    n = len(nums) - 1
    left = right = k
    smallest = nums[k]
    while (left != 0 or right != n):
        if left == 0:
            right += 1
            smallest = min(smallest, nums[right])
        elif right == n:
            left -= 1
            smallest = min(smallest, nums[left])
        elif nums[right + 1] > nums[left - 1]:
            right += 1
            smallest = min(smallest, nums[right])
        else:
            left -= 1
            smallest = min(smallest, nums[left])
        temp = smallest * (right - left + 1)
        ans = max(ans, temp)
    return ans