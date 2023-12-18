from collections import deque

def isInterleave(s1, s2, s3):
    r, c, l= len(s1), len(s2), len(s3)
    if r+c != l:
        return False
    queue, visited = deque((0, 0)), set((0, 0))
    while queue:
        x, y = queue.popleft()
        if x+y == l:
            return True
        if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
            queue.append((x+1, y)); visited.add((x+1, y))
        if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
            queue.append((x, y+1)); visited.add((x, y+1))
    return False

ss1 = "aabcc"
ss2 = "dbbca"
ss3 = "aadbbcbcac"

print(isInterleave(ss1, ss2, ss3))