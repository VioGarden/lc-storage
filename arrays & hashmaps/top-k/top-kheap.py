from collections import defaultdict, heapq

def topKFrequent(nums, k):
    hashmap = defaultdict(int)
    for i in nums:
        hashmap[i] += 1
    
    heap = []
    for key, val in hashmap.items():
        heapq.heappush(heap, (-val, key))
    
    result = []
    for i in range(k):
        result.append(heapq.heappop(heap)[1])
        if len(result) == k:
            return result
    