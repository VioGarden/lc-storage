from collections import heapq

def minimumEffortPath(heights):
    """
    :type heights: List[List[int]]
    :rtype: int
    """
    rows, cols = len(heights), len(heights[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    min_heap = [[0, (0, 0)]] # cost, x_pos, y_pos
    visited = { (0, 0): 0 } # pos : cost
    end_game = (rows - 1, cols - 1)

    while min_heap:
        cost, position = heapq.heappop(min_heap)
        if position == end_game:
            return visited[position]
        curr_x, curr_y = position
        temp_cost = heights[curr_x][curr_y]
        for d in directions:
            new_x, new_y = curr_x + d[0], curr_y + d[1]
            if 0 <= new_x < rows and 0 <= new_y < cols:
                new_cost = max(cost, abs(heights[new_x][new_y] - temp_cost))
                if (new_x, new_y) not in visited or ((new_x, new_y) in visited and visited[(new_x, new_y)] > new_cost):
                    visited[(new_x, new_y)] = new_cost
                    heapq.heappush(min_heap, [new_cost, (new_x, new_y)])
    # return visited[end_game]