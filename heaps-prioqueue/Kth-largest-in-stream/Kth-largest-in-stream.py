import heapq

class KthLargest:
    def __init__(self, k, nums):
        # minheap with K largest integers    # (n-k)(logN) --> nlogn
        self.minHeap, self.k = nums, k # constructor, create minHeap and init k
        heapq.heapify(self.minHeap) # turns into array Heap, creates sorted property (n)
        while len(self.minHeap) > k:  # while minheap size > k, pop smallest elements (logn)
            heapq.heappop(self.minHeap)
        # (n)(logn) --> NlogN

    def add(self, val):
        heapq.heappush(self.minHeap, val) # add function (logn), 1) add to minheap
        if len(self.minHeap) > self.k: # edge case if size of minheap less than k
            heapq.heappop(self.minHeap) # 2) pop from minheap
        return self.minHeap[0] # min value in heap is always stored in index [0] (sorted)
        

# MinHeap
#     -Add O(logN)
#     -Pop O(logN)
#     -min O(1)