from collections import deque

def hasPathSum(root, targetSum):
    if not root:
        return False
    q = deque([(root, targetSum - root.val)])
    while q:
        curr, val = q.popleft()
        if not curr.left and not curr.right and val == 0:
            return True
        if curr.left:
            q.append((curr.left, val - curr.left.val))
        if curr.right:
            q.append((curr.right, val - curr.right.val))
    return False