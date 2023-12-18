# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: # if the subtree is empty, of course it is a subtree, so return True
            return True
        if not root: # if the root tree is empty, (^ already settled t is empty), return False
            return False  # order matters, this if statement goes below first if statement
        # checked for emptiness in subtree and root tree
        if self.sameTree(root, subRoot): # comparing tree, if equal, return True
            return True 
        # if they are not the same tree (compare subRoot to root tree right or left recursively)
        # if one of these are true, return True
        # recursive call (calling until self.sameTree possibly returns true a few lines above)
        return (self.isSubtree(root.left, subRoot) or # subRoot to root tree left
            self.isSubtree(root.right, subRoot)) # subRoot to root tree right 

    
    def sameTree(self, s, t): # helper recursive function, two trees, see if they are the same thing
        if not s and not t: # if both are empty, same tree, return True
            return True
        if s and t and s.val == t.val:  # if both are non-empty, and values are the same
            return (self.sameTree(s.left, t.left) and # want to know if left subtrees are the same
                self.sameTree(s.right, t.right))   # want to know if right subtrees are the same
        return False   # if one of them don't work, return False

# careful of edgecases
# keep track if trees have extra leaf
# a null subtree is a subtree of another subtree
# need helper function
