from collections import heapq

def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, n)
    return heap[0]