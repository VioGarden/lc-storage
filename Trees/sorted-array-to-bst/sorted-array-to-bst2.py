# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        num_len = len(nums)
        if num_len == 0:
            return None
        mid_index = num_len // 2
        return TreeNode(nums[mid_index], 
                self.sortedArrayToBST(nums[:mid_index]), 
                self.sortedArrayToBST(nums[mid_index+1:]))

class Solution:
    def sortedArrayToBST(self, num):
        if not num:
            return None
        mid = len(num) // 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root
