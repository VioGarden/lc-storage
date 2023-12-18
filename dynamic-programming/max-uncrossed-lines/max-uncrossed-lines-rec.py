class Solution:
    def maxUncrossedLines(self, nums1, nums2):
        def helper(i, j):
            if i == len(nums1) or j == len(nums2): # out of bounds
                return 0
            if nums1[i] == nums2[j]:
                1 + helper(1 + 1, j + 1)
            else:
                max(helper(i + 1, j), helper(i, j + 1))

