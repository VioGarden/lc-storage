def countNicePairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [value - int(str(value)[::-1]) for value in nums]
    hashmap = {}
    for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)
    ans = 0
    for n in hashmap.values():
        ans += n * (n - 1)//2
    return ans % (10**9 + 7)

    # ans, hashmap = 0, defaultdict(int)
    # for index, value in enumerate(nums):
    #     k = value - int(str(value)[::-1])
    #     print(value, int(str(value)[::-1]), k)
    #     ans += hashmap[k]
    #     hashmap[k] += 1
    # return ans % (10**9 + 7)