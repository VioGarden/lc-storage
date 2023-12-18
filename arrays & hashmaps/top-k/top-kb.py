def topKFrequent(self, nums, k):
    hashmap = {}
    for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)
    x = list(hashmap.items())
    y = sorted(x, key=lambda x: x[1], reverse=True)
    result = []
    for i in range(k):
        result.append(y[i][0])
    return result