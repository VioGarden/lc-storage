from collections import deque

def maxSlidingWindow(nums, k):
    q = deque() # create deque
    output = [] # create output

    for index, value in enumerate(nums): # iterate through (amortized O(n))

        while (q and value > nums[q[-1]]): # want to pop from end of queue if new value is greater than value at end of queue
            q.pop()

        if (q and q[0] < (index - k + 1)): # if window is slid over a value, remove from end of queue
            q.popleft()

        q.append(index) # add current to end of q

        output.append(nums[q[0]]) # element at front of queue should be the one with the gretest value
    
    return output[k-1:] # since this calculated for every single one, output is k-1:end