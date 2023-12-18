class Solution:
    def rob(self, nums): 
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, num): # base house robber
        r1, r2 = 0, 0
        for i in num:
            # [r1, r2, i, i + 1...]
            temp = max(r1 + i, r2)
            r1 = r2
            r2 = temp
        return r2
    