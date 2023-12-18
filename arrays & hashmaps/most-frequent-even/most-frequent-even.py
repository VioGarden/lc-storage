def mostFrequentEven(nums):
    hashmap = {}
    ans, count = float(999999999999999999), 0 # float(inf)
    for i in nums:
        if i % 2 == 0:
            hashmap[i] = hashmap.get(i, 0) + 1
            if (hashmap[i] > count) or (hashmap[i] == count and i < ans):
                ans, count = i, hashmap[i]
    
    return -1 if count == 0 else ans
