from collections import deque

def maxLevelSum(root):
    level = 0
    highest = root.val
    answer = 1
    q = deque()
    q.append(root)
    while q:
        level += 1
        current_count = 0
        for _ in range(len(q)):
            curr = q.popleft()
            current_count += curr.val
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        if current_count > highest:
            highest = current_count
            answer = level
    
    return answer
        