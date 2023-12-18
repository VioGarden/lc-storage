def maxArea(height):
    left, right = 0, len(height) - 1 # initialize left and right pointers
    area = 0 # initial area 0
    while left < right: # while pointers don't cross
        new = min(height[left], height[right]) * (right - left) # calculate area
        area = max(new, area) # area is the greater of old and new
        if height[left] > height[right]: # if left is bigger and right is smaller
            right -= 1 # decrement right
        else:
            left += 1 # if left is smaller, increment
    return area # return

print(maxArea([1,8,6,2,5,4,8,3,7]))