def maxSlidingWindow(nums, k):
    output = []
    for i in range(k - 1, len(nums)):
        curr = []
        for j in range(i - (k - 1), i + 1):
            curr.append(nums[j])
        output.append(max(curr))

    return output