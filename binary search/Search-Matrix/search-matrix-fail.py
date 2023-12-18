def searchMatrix(matrix, target):
    left, right = 0, len(matrix) - 1
    while left < right:
        mid = (right + left)//2
        print(matrix[mid][0])
        if matrix[mid][1] > target:
            right = mid - 1
        elif matrix[mid][1] < target:
            left = mid + 1
        else:
            return True
    numSet = set(matrix[left])
    if target in numSet:
        return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 2))