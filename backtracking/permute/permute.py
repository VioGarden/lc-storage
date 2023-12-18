class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [nums[:]]
        result = []
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for p in perms:
                p.append(n)
            result.extend(p)
            nums.append(n)
        return result