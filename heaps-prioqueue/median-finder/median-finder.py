from collections import heapq

class MedianFinder:

    def __init__(self):
        # heaps are initialized as lists
        self.small = [] # small heap will be max heap (highest O(1))
        self.large = [] # large heap will be min heap (lowest O(1))

    def addNum(self, num: int) -> None:
        # when number is added, added to smaller heap
        heapq.heappush(self.small, (-1*num))
        
        # if the max
        if (self.small and self.large and # existence of  both heaps
            # if max heap value of small heap > mix heap value of large heap
           (self.small[0]*-1) > self.large[0]):
           # change that value from min to max heap
            top = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, top)
            
        # if small heap is 2+ lengths longer than min heap
        if len(self.small) > 1 + len(self.large):
            # flip value
            top = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, top)
                           
        # if large heap is 2+ lengths longer than min heap
        if len(self.large) > 1 + len(self.small):
            # flip heap
            top = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * top)

    def findMedian(self) -> float:
        # if small heap longer than large heap, median in small heap
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        # if large heap longer than small heap, meadian in large heap
        if len(self.large) > len(self.small):
            return self.large[0]
        # if even lengths, find center
        return (self.small[0] * -1+self.large[0])/2
        