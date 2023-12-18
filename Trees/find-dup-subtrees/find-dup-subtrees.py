from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        checked = defaultdict(int)
        final = []

        def helper(node):
            if not node:
                return
            curr = (helper(node.left), node.val, helper(node.right))
            if curr in checked and checked[curr] == 1:
                print(node)
                final.append(node)
            checked[curr] += 1
            return curr
        
        helper(root)
        return final
            