def subsetsWithDup(nums):
    final = []
    nums.sort()
    
    def recursive(n, curr=[]):
        if n == len(nums):
            final.append(curr[::])
            return
        
        curr.append(nums[n])
        recursive(n + 1, curr)
        curr.pop()
        
        while n < len(nums) - 1 and nums[n + 1] == nums[n]:
            n += 1
        recursive(n + 1, curr)
    recursive(0, [])
    
    return final

# x = [4,2,2,2,2]
# print(subsetsWithDup(x))