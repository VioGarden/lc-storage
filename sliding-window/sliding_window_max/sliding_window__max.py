from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()

    output = []

    for index, number in enumerate(nums):

        while (q and number > nums[q[-1]]):
            q.pop()
        
        if (q and index - q[0] >= k):
            q.popleft()
        
        q.append(index)

        output.append(nums[q[0]])
    
    return output[k-1:]