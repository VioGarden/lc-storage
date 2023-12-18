from collections import heapq

def reorganizeString(s):
    hashmap = {}
    for i in s:
        hashmap[i] = 1 + hashmap.get(i, 0)
    # python will heapify based on first value
    maxHeap = [[-count, char] for char, count in hashmap.items()]
    heapq.heapify(maxHeap) # O(n)
    prev = None
    res = ""
    while maxHeap or prev:

        if prev and not maxHeap: # where prev something, but heap is empty
            return ""

        count, char = heapq.heappop(maxHeap)
        res += char
        count += 1

        if prev:
            heapq.heappush(maxHeap, prev)
            prev = None

        if count != 0:
            prev = [count, char]
    return res
