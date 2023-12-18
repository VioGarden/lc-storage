# memoization O(n*m)

class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        def helper(i, j):
            if i == len(nums1) or j == len(nums2): # out of bounds
                return 0
            if (i, j) in hashmap:
                return hashmap[(i, j)]
            if nums1[i] == nums2[j]:
                hashmap[(i, j)] = 1 + helper(i + 1, j + 1)
            else:
                hashmap[(i, j)] = max(helper(i + 1, j), helper(i, j + 1))
            return hashmap[(i, j)]
        hashmap = {}
        return helper(0, 0)