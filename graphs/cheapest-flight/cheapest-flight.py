def findCheapestPrice(n, flights, src, dst, k):
    same_starts = [[] for _ in range(n)]
    for f in flights:
        same_starts[f[0]].append((f[1], f[2]))
    final = [float('inf') for _ in range(n)]
    q = [(src, 0)]
    stops = 0
    while q and stops <= k:
        size = len(q)
        for i in range(size):
            curr_node, cost = q.pop(0)
            for neighbor, price in same_starts[curr_node]:
                if final[neighbor] <= cost + price:
                    continue
                final[neighbor] = price + cost
                q.append((neighbor, final[neighbor]))
        stops += 1
    return -1 if final[dst] == float('inf') else final[dst]


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))