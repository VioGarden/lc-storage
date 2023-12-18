class Solution:
    def subsets(self, nums):
        final = []
        present = []
        def dfs(n):
            if n >= len(nums):
                final.append(present[:])
                return
            
            present.append(nums[n])
            dfs(n + 1)

            present.pop()
            dfs(n + 1)
        dfs(0)
        return final
