# breadth first search

import collections


def numIslands(grid):
    if not grid: # if empty grid, just return 0
        return 0

    rows, cols = len(grid), len(grid[0]) # length of rows and columns
    visit = set() # mark positions visited (use set (2-D grid also works))
    islands = 0 # islands initilize to 0

    def bfs(r, c):  # bfs is iterative not recursive, so use q queue (normally)
        q = collections.deque()
        visit.add((r,c)) # marks a visited cell
        q.append((r,c)) # add visited cell

        while q: # while q is not empty, expanding island
            row, col = q.popleft() # pop from queue (bfs)
            # row, col = q.pop() # depth first search
            directions = [[1, 0], [-1, 0], [0,1], [0, -1]] # check adjacent islands
            for dr, dc in directions: # for each of directions
                # r, c are the new coordinates we want to check
                r, c = row + dr, col + dc
                # check if in bounds (r in range and c in range)
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == "1" and # if island is a 1 (valid)
                    (r, c) not in visit): # and the tuple has not already been visited
                    q.append((r, c)) # if valid island, must add to queue
                    visit.add((r, c)) # if valid island, must add to visited

    for r in range(rows): # iterate through 2-D list
        for c in range(cols):
            # if found cell is an island and hasn't been visited
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c) # apply a breadth first search to see how big it is
                islands += 1 # addind to total island count for new island found
    return islands



# another way is to change the actual grid[r][c] to like -2
# instead of adding found position to a map

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1