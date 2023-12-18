# def searchMatrix(matrix, target):
#     # ROWS, COLS = len(matrix), len(matrix[0]) # rows and cols

#     # top, bot = 0, ROWS - 1 # finding correct array
#     # while top <= bot: # while pointers dont pass each other
#     #     row = (top + bot) // 2 # mid point
#     #     if target > matrix[row][-1]: 
#     #         top = row + 1
#     #     elif target < matrix[row][0]:
#     #         bot = row - 1
#     #     else:
#     #         break

#     # if not (top <= bot):
#     #     return False
    
#     # row = (top + bot)//2
#     # l, r = 0, COLS - 1
#     # while l <= r:
#     #     m = (1 + r)//2
#     #     if target > matrix[row][m]:
#     #         l = m + 1
#     #     elif target < matrix[row][m]:
#     #         r = m - 1
#     #     else:
#     #         return True
#     # return False