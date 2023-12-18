def subarraysDivByK(nums, k):
    final = 0
    hashmap = {}
    current = 0
    hashmap[0] = 1
    for i in range(len(nums)):
        current += nums[i]
        div_remains = current%k
        if hashmap.get(div_remains) != None:
            val = hashmap.get(div_remains)
            final += val
            hashmap[div_remains] = val + 1
        else:
            hashmap[div_remains] = 1
    return final

subarraysDivByK([4,5,0,-2,-3,1], 5)