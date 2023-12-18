# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:  # if both trees are empty, same tree so True
            return True
        if not p or not q: # if only one of them are null, different, so False
            return False
        if p.val != q.val: # if values of root do not match, return False
            return False
        return (self.isSameTree(p.left, q.left) and # if and is True, returns True, else, returns False
                self.isSameTree(p.right, q.right)) # recursive call on everything
        