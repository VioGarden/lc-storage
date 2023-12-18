def searchMatrix(matrix, target):
    left, right = len(matrix) - 1, len(matrix[0]) - 1
    while left <= right:
        mid = (left + right)//2
        if matrix[mid][-1] < target:
            left = mid + 1
        elif matrix[mid][0] > target:
            right = mid - 1
        else:
            break
    row = (left + right)//2
    rleft, rright = 0, len(matrix[row])
    while rleft < rright:
        mid2 = (rright + rleft)//2
        if matrix[row][mid2] < target:
            left = mid2 + 1
        elif matrix[row][mid2] > target:
            right = mid2 - 1
        else:
            return True
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 2))
