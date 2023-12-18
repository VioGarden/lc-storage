# steps
# pointers start at end, value is min(left bar, right bar) * width
# shift pointer from whichever bar is lower
# see is total is greater than saved total

def maxArea(height):
    left, right, width = 0, len(height) - 1, len(height) -1
    total = min(height[left], height[right]) * width
    while left < right:
        new = min(height[left], height[right]) * width
        if total < new:
            total = min(height[left], height[right]) * width
        if height[right] >= height[left]:
            left += 1
            width -= 1
        else:
            right -= 1
            width -= 1
    return total

print(maxArea([1,8,6,2,5,4,8,3,7]))