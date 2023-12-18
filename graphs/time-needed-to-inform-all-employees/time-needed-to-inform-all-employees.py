from collections import defaultdict, heapq

def numOfMinutes(n, headID, manager, inform_time):
    graph = defaultdict(list)

    for i, manager_id in enumerate(manager):
        graph[manager_id].append((inform_time[i], i))
    
    dist = {}
    heap = [(inform_time[headID], headID)]

    while heap:
        time, u = heapq.heappop(heap)
        if u in dist:
            continue
        dist[u] = time
        for w, v in graph[u]:
            if v in dist:
                continue
            heapq.heappush(heap, (time + w, v))
    return max(dist.values())