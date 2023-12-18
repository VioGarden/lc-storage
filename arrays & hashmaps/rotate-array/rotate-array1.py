
def rotate(nums, k):
    k = k % len(nums) # modulus if k is bigger than length of nums
    
    l, r = 0, len(nums) - 1  # left right pointers to start and end of nums
    while l < r: 
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = 0, k - 1 # left and right pointers to start and k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = k, len(nums) - 1 # left and right pointers to k and end
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
