def rob(nums):
    if len(nums) == 1: # if len of nums is one, return nums[0]
        return nums[0]
    
    def helper(num): # helper function for base house robber
        rob1, rob2 = 0, 0
        for n in num:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    word = max(helper(nums[1:]), helper(nums[:-1])) # run on both of these
    
    return word
    