from collections import defaultdict
import math

def maxPoints(points):
    if len(points) <= 2:
        return len(points)

    def distance(a, b):
        x1, y1 = a
        x2, y2 = b
        if x1 - x2 == 0:
            return math.inf
        return (y1 - y2)/(x1 - x2)
        
    length = 1
    for index, point in enumerate(points):
        slopes = defaultdict(int)
        for jpoint in points[index+1:]:
            slope = distance(point, jpoint)
            slopes[slope] += 1
            length = max(length, slopes[slope])
    return length + 1