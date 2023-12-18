# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0] # global variable

        def dfs(root): # recursion time
            if not root:
                return -1 # null tree height is -1
            left = dfs(root.left) # height of left subtree
            right = dfs(root.right) # height of right subtree

            res[0] = max(res[0], 2 + left + right)
            # height : 2 + left + right (diameter)
            return 1 + max(left, right) # return height running thru root

        dfs(root) # call function
        return res[0] # return result
        

# bottom up approach