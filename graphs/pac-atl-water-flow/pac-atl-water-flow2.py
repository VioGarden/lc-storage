def pacificAtlantic(heights):
    if not heights:
        return []
    
    rows = len(heights)
    cols = len(heights[0])
    
    visit = set()
    
    def dfs(start):
        r, c = start
        temp = (r,c)
        if temp in visit:
            return
        visit.add(temp)
        # start is tuple, visit and flow are seyts
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        curr_val = heights[r][c]
        for i in directions:
            row = r + i[0]
            col = c + i[1]
            if ((row,col) not in visit and
                0 <= row and
                row <= rows - 1 and
                0 <= col and
                col <= cols - 1 and
                heights[row][col] >= curr_val): 
                    visit.add((r,c))
                    dfs((row, col))
    
    for i in range(cols):
        inp = (0, i)
        dfs(inp)
    
    for j in range(0, rows):
        inp = (j, 0)
        dfs(inp)
        
    pac_list = list(visit)
    
    visit.clear()
    
    for k in range(rows):
        inp = (k, cols - 1)
        dfs(inp)
        
    for l in range(cols):
        inp = (rows - 1, l)
        dfs(inp)
    
    both = []
    for i in pac_list:
        if i in visit:
            both.append(list(i))
    return both
    

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

pacificAtlantic(heights)