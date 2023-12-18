class Solution:
    def threeSum(self, n, tar):
        final3 = []
        n.sort()
        for i in range(len(n) - 2):
            left = i + 1
            right = len(n) - 1
            t = tar - n[i]
            if i == 0 or n[i] != n[i-1]:
                while left < right:
                    s = n[left] + n[right]
                    if s == t:
                        final3.append([n[i], n[left], n[right]])
                        while left < right and n[left] == n[left + 1]:
                            left += 1
                        while left < right and n[right] == n[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif s > t:
                        right -= 1
                    else:
                        left += 1
        return final3                 
                
    def fourSum(self, nums,target):
        final4 = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                final333 = self.threeSum(nums[i+1:], target-nums[i])
                for thing in final333:
                    final4.append([nums[i]] + thing)
        return final4
                
            