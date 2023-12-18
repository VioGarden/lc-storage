def hasPathSum(root, targetSum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right and val == targetSum:
            return True
        if curr.left:
            stack.append((curr.left, val + curr.left.val))
        if curr.right:
            stack.append((curr.right, val + curr.right.val))
    return False