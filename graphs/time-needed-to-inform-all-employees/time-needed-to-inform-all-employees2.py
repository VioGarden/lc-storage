from collections import defaultdict, deque

def numOfMinutes(n, headID, manager, informTime):
    adj = defaultdict(list)
    for i in range(n):
        adj[manager[i]].append(i)

    q = deque([(headID, 0)])
    res = 0
    while q:
        i, time = q.popleft()
        res = max(res, time)
        for emp in adj[i]:
            q.append((emp, time + informTime[i]))
    
    return res