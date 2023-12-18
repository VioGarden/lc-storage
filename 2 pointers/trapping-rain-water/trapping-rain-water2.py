def trap(height):
    # left pointer, right pointer, total
    left, right, total = 0, len(height) - 1, 0 
    # max of left and right
    maxleft, maxright = 0, 0
    # instead of left < right, left <= right, while left doesnt pass right
    while left <= right:
        # which ever end is lower, work on that end
        if maxleft <= maxright:
            # store is difference between max possible and height
            store = maxleft - height[left]
            # if store is positive
            if store > 0:
                # add to score
                total += store
            # update max to the higher one
            maxleft = max(maxleft, height[left])
            # update iterable
            # careful of not incrementing too early, when to incremenet
            left += 1
        else:
            # store is max boundary subtracting height
            store = maxright - height[right]
            # if boundary is higher than space for water
            if store > 0:
                # add that difference to score
                total += store
            # maxright is maximum value for maxright, and height
            maxright = max(maxright, height[right])
            # decrement variable
            # careful of not incrementing too early, when to incremenet
            right -= 1
    # returning total
    return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))