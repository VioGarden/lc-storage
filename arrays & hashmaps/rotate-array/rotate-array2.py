
def rotate(nums, k):
    k = k % len(nums)
    
    reverse(0, len(nums) - 1) # reverses entire array
    reverse(0, k - 1) # reverses first k - 1 elements (k elements)
    reverse(k, len(nums) - 1) # reverses the rest of the array

    def reverse(left, right): # reversing function
        while left < right: # while left pointer is less than right
            nums[left], nums[right] = nums[right], nums[left] # flip the nums of left and right
            left, right = left + 1, right - 1 # increment pointer by one