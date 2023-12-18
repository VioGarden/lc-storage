from collections import defaultdict
import math

def maximumDetonation(bombs):
    adj = defaultdict(list)
    for i in range(len(bombs)):
        for j in range(i + 1, len(bombs)):
            x1, y1, r1 = bombs[i]
            x2, y2, r2 = bombs[j]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            if distance <= r1:
                adj[i].append(j)
            if distance <= r2:
                adj[j].append(i)

    def dfs(i, visit):
        if i in visit:
            return 0
        visit.add(i)
        for nei in adj[i]:
            dfs(nei, visit)
        return len(visit)
    

    res = 0
    for i in range(len(bombs)):
        res = max(res, dfs(i, set()))
    return res