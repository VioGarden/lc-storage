# Definition for a binary tree node.
# recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res
        
    def dfs(self, roar, path):
        if not roar.right and not roar.left:
            self.res += (path*10 + roar.val)
        if roar.right:
            self.dfs(roar.right, path*10 + roar.val)
        if roar.left:
            self.dfs(roar.left, path*10 + roar.val)
        