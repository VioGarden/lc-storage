def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    graph = {}
    for prev, curr in tickets:
        if prev in graph:
            graph[prev].append(curr)
        else:
            graph[prev] = [curr]
    
    for elem in graph.keys():
        graph[elem].sort(reverse=True)
    
    stack = ["JFK"]
    ans = []

    while stack:
        temp = stack[-1]
        if temp in graph and len(graph[temp]) > 0:
            stack.append(graph[temp].pop())
        else:
            ans.append(stack.pop())
    
    return ans[::-1]