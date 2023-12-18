from collections import heapq

def reorganizeString(s):
    hashmap = {}
    final = ""

    for i in s:
        hashmap[i] = 1 + hashmap.get(i, 0)
    
    maxHeap = [(-value, key) for key, value in hashmap.items()]
    heapq.heapify(maxHeap)

    holder = None

    while maxHeap or holder:
        if holder and not maxHeap:
            return ""
        count, char = heapq.heappop(maxHeap)
        if holder:
            heapq.heappush(maxHeap, holder)
            holder = None
        final += char
        if count + 1 < 0:
            holder = (count + 1, char)
        
    return final