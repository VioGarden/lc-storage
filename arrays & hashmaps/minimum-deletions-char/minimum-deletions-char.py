from collections import heapq

def minDeletions(s):
    hashmap = {}
    for i in s:
        hashmap[i] = 1 + hashmap.get(i, 0)
    bucket = [False] * (len(s) + 1)
    arr = []
    for i in hashmap.values():
        if i > 0:
            arr.append(-i)
    heapq.heapify(arr)
    ans = 0
    while arr:
        curr = heapq.heappop(arr)
        if not bucket[-curr]:
            bucket[-curr] = True
        elif curr == 0:
            pass
        else:
            heapq.heappush(arr, curr + 1)
            ans += 1
    return ans