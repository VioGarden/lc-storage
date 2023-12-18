# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        def valid(node, left, right):
            if not node: # if leaf, True
                return True

            if not (left < node.val and node.val < right): # is val is not in range, return False
                return False

            return (valid(node.left, left, node.val) and # check ranges
            valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))


# other solution is to do an in-order traversal and check the result. If resulting array is in ascending order, it is a valid binary search tree.