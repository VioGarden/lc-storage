import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # only minheaps exist in python
        stones = [-s for s in stones] # create negative array of stones
        heapq.heapify(stones) # create the heap
        
        while len(stones) > 1: # while heap array has more than 1 stones
            first = heapq.heappop(stones) # pop the first
            second = heapq.heappop(stones) # pop the second
            # remember the backwardsness, second = -7 first = -8 
            if second > first: # is second is greater than first
                heapq.heappush(stones, first - second) # push the difference
        
        if not stones: # if two stones remained and cancelled each other out
            return 0 # return 0
        return abs(stones[0]) # retrun abs cause worked with negatives