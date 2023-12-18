def findSmallestSetOfVertices(n, edges):
    return list(set(range(n)) - set(j for i, j in edges))

def findSmallestSetOfVertices(n, edges):
    result = set(range(n))
    for i, j in edges:
        if j in result:
            result.remove(j)
    return list(result)