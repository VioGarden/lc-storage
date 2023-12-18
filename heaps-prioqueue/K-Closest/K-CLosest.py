import heapq

def kClosest(points, k):
    amazing = []
    for i in points:
        distance = (i[0]**2 + i[1]**2)
        amazing.append([distance, i])
    heapq.heapify(amazing)
    final = []
    for i in range(k):
        thing = heapq.heappop(amazing)
        final.append(thing[1])
    return final
            
points = [[1,3],[-2,2]]
k = 1

kClosest(points, k)

