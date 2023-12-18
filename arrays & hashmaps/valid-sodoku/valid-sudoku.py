from collections import defaultdict

def isValidSudoku(board):
    #set, {'list','of','unique','items'}
    cols = defaultdict(set) #initialize hash set, key : column | value : set of values
    rows = defaultdict(set) #initialize hash set, key : row | value : set of values
    squares = defaultdict(set)  # key : (tuple) (r//3, c//3) | value : set of values
    
    #iterating through whole sudoku once
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":    #. is an empty value in the sudoku
                continue      #next iteration in loop
            if (board[r][c] in rows[r] or  #if value in board found in rows[#]:{here}
                board[r][c] in cols[c] or  #if value in board found in cols[#]:{here}
                board[r][c] in squares[(r//3,c//3)]): #if value in board found in squares(#,#):{here}
                return False
            cols[c].add(board[r][c])   #add to cols[#]:{}
            rows[r].add(board[r][c])   #add to rows[#]:{}
            squares[(r//3,c//3)].add(board[r][c])  #add to squares[(#,#)]:{}
    return True   #no false statements, return True

print(isValidSudoku(
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

#output : False