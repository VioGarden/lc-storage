def firstMissingPositive(nums):
    lowest_pos = min(nums)
    highest_pos = max(nums)
    if highest_pos < 1:
        return 1
    if lowest_pos > 1:
        return 1
    
    lowest_pos = highest_pos
    for i in nums:
        if i < 1:
            continue
        if i < lowest_pos:
            lowest_pos = i
    if lowest_pos != 1:
        return 1
    nums = set(nums)
    while (lowest_pos + 1) in nums:
        lowest_pos += 1
    
    return (lowest_pos + 1)