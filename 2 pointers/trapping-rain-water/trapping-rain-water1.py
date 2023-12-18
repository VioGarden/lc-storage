def trap(height):
    if not height: return 0
    # left, right pointers initialized to index of edges
    left, right = 0, len(height) - 1
    # leftMax and rightMax initialized to values of edges
    leftMax, rightMax = height[left], height[right]
    # result is 0
    result = 0

    # while pointer left is less than right
    while left < right:
        # if value of left is lower than right
        if leftMax < rightMax:
            # pointer +1
            left += 1
            # compare hight to previous height, possible new value to leftMax
            leftMax = max(leftMax, height[left])
            # leftMax updated in line above, value will never be negative
            result += leftMax - height[left]
        else:
            # pointer -1
            right -= 1
            # rightMax (boundary) is max(former boundary, new boundary)
            rightMax = max(rightMax, height[right])
            # max - new boundary
            result += rightMax - height[right]
    return result
# think of it like this
# max(old boundary, new boundary)
# if new boundary is bigger, new boundary - new boundary = 0
# if new boundary is same, new boundary - new boundary = 0
# if new boundary is less, old boundary - new boundary = 1

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))