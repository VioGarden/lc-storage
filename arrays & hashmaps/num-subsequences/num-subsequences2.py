def numSubseq(nums, target):
    total = 0
    nums.sort()
    num_len = len(nums)
    for i in range(num_len):
        if nums[i]*2 > target:
            break
        curr_count = 0
        j = i + 1
        while j < len(nums) and (nums[i] + nums[j]) <= target:
            j += 1
            curr_count += 1
        print("hi", nums[i], curr_count)
        total += pow(2, curr_count, 10**9+7)
    return total  % (10**9 + 7)


# code good, just time limit exceeded
