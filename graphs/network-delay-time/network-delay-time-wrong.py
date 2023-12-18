from collections import defaultdict, heapq

def networkDelayTime(times, n, k):
    
    graph = defaultdict(list)

    for source, target, time in times:
        graph[source].append((target, time))

    priority_queue = [(0, k)] # (time, source) ~~ imporant that time comes first
    visit = set()
    t = 0
    while priority_queue:
        time_time, k_k = heapq.heappop(priority_queue)
        if k_k in visit:
            continue
        visit.add(k_k)
        t = max(t, time_time)

        for target2, time2 in graph[k_k]:
            if target2 not in visit:
                heapq.heappush(priority_queue, (time2 + time_time, target2))
    
    return t if len(visit) == n else -1