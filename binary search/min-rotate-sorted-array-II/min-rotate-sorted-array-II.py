def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            if nums[mid] < nums[left]:
                right = mid
            else:
                right -= 1
    return nums[left]