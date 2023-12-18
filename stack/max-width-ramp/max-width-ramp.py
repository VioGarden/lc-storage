def maxWidthRamp(nums):
    stack = []
    for index, value in enumerate(nums):
        if not stack or nums[stack[-1]] > value:
            stack.append(index)

    maximum_width = 0
    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            maximum_width = max(maximum_width, i - stack.pop())
    
    return maximum_width