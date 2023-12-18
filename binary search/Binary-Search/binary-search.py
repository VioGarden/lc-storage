def search(nums, target):
    """sorted list, find target"""
    # initialize pointers to edges
    left, right = 0, len(nums) - 1
    # while left pointer isn't greater than right pointer
    while left <= right:
        # mid = left + (right - left)//2  #if left + right greater than boundary
        mid = (left + right)//2
        # if target is found, return
        if nums[mid] == target:
            return mid
        # if midpoint number is less than target
        elif nums[mid] < target:
            # left boundary is mid + 1
            left = mid + 1
        # if right number is greater than target
        else:
            # right boundary is mid - 1
            right = mid - 1

    # if target is not found, return -1
    return -1