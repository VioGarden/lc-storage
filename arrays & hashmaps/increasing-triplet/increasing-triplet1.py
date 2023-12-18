def increasingTriplet(nums):
    one, two, curr = 0, 0, 0
    while curr < len(nums):
        if two != 0 and nums[curr] > nums[two]:
            return True
        if nums[curr] > nums[one]:
            two = curr
        if nums[curr] < nums[one]:
            one = curr
        curr += 1
    return False

