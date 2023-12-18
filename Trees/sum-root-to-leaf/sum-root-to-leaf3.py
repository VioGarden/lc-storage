# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        stack, final = [[root, 0]], 0
        while stack:
            rootroot, current = stack.pop()
            maybe_next = rootroot.val + current*10
            if not rootroot.right and not rootroot.left:
                final += maybe_next
            if rootroot.right:
                stack.append([rootroot.right, maybe_next])
            if rootroot.left:
                stack.append([rootroot.left, maybe_next])
        return final
        