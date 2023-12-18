def sortColors(nums):
    left, right = 0, len(nums) - 1
    i = 0
    
    def swap(a,b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
    
    while i <= right:
        if nums[i] == 0:
            swap(left, i)
            left += 1
        elif nums[i] == 2:
            swap(i, right)
            right -= 1
            i -= 1
        i += 1
            