def productExceptSelf(nums):
    bucket = [[] for i in range(len(nums))]
    for i in range(len(nums)):
        for j in range(len(bucket)):
            if i != j:
                bucket[j].append(nums[i])
    
    result = []
    for i in range(len(bucket)):
        count = 1
        for j in bucket[i]:
            count *= j
        result.append(count)

#brute force method