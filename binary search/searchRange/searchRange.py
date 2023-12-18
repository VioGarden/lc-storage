def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    left1, right1 = 0, len(nums) - 1
    while left1 < right1:
        mid = (left1 + right1)//2
        if nums[mid] < target:
            left1 = mid + 1
        else:
            right1 = mid
    if nums[left1] != target:
        return [-1, -1]
    # final_left = left1
    # while left1 < (len(nums) - 1) and nums[left1 + 1] == nums[left1]:
    #     left1 += 1
    # return [final_left, left1]

    left2, right2 = 0, len(nums) - 1
    while left2 < right2:
        mid = -((-left2 - right2)//2)
        if nums[mid] > target:
            right2 = mid - 1
        else:
            left2 = mid
    return [left1, right2]