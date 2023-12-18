from collections import heapq

# string answer

def kthLargestNumber(nums, k):
    array = [-int(x) for x in nums]
    heapq.heapify(array)
    while k > 1:
        heapq.heappop(array)
        k -= 1
    result = heapq.heappop(array)
    return str(-result)

