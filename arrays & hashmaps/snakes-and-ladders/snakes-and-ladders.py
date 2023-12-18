from collections import deque
def snakesAndLadders(board):
    n = len(board)
    def getRowCol(position):
        row = (position - 1)//n
        col = (position - 1)%n
        if row % 2 == 0:
            return n-1-row, col
        return n-1-row, n-1-col
    
    visited = set()
    queue = deque([])
    queue.append((1,0))
    while queue:
        position, rolls = queue.popleft()
        r, c = getRowCol(position)
        if board[r][c] != -1:
            position = board[r][c]
        if position == n**2:
            return rolls
        for i in range(1, 7):
            next_pos = position + i
            if (next_pos) not in visited and (next_pos) <= n**2:
                visited.add(next_pos)
                queue.append((next_pos, rolls + 1))

    return -1