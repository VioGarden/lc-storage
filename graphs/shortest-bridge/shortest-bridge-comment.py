def shortestBridge(grid):
    # Determine the size of the grid
    n = len(grid)
    
    # Depth-first search (DFS) function to mark connected components
    def dfs(i, j):
        # Mark the current cell as visited (-1)
        grid[i][j] = -1
        # Add the current cell to the breadth-first search (BFS) queue
        bfs.append((i, j))
        # Explore the neighboring cells
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            # Check if the neighboring cell is within the grid boundaries and is part of the island (marked as 1)
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                # Recursively call the DFS function on the neighboring cell
                dfs(x, y)
    
    # Helper function to find the first island (connected component)
    def first():
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    # Return the coordinates of the first cell in the island
                    return i, j
    
    # Initialize the step counter and the BFS queue
    step = 0
    bfs = []
    
    # Perform DFS to mark the first island
    dfs(*first())
    
    # BFS to find the shortest bridge to the second island
    while bfs:
        # Create a new queue for the next step
        new = []
        # Process each cell in the current BFS queue
        for i, j in bfs:
            # Explore the neighboring cells
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # Check if the neighboring cell is within the grid boundaries
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        # If the neighboring cell belongs to the second island, return the current step
                        return step
                    elif not grid[x][y]:
                        # If the neighboring cell is unvisited (marked as 0), mark it as visited (-1)
                        grid[x][y] = -1
                        # Add the neighboring cell to the new BFS queue
                        new.append((x, y))
        
        # Increment the step counter
        step += 1
        # Replace the current BFS queue with the new queue for the next step
        bfs = new
 