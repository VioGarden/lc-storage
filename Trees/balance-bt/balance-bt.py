# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):

        def dfs(root): # recursive returns boolean and height
            if not root:  # base case
                return [True, 0] # empty tree, balanced and height 0
            left, right = dfs(root.left), dfs(root.right) # determine if right/left balanced
            balanced = (left[0] and right[0] and  # balanced from root node
                abs(left[1] - right[1]) <= 1)  # <-- balanced AND if True for zero indeces
            return [balanced, 1 + max(left[1], right[1])] # return [is true balanced? T/F, height]

                # above is only true if left, right AND root subtree is balanced
        return dfs(root)[0] # want to return boolean

# bottom up approach


        