def searchMatrix(matrix, target):

    rows, cols = len(matrix), len(matrix[0]) # this gets length of rows and cols
    # left is zero, rows * cols gives full length - 1 to get index
    left, right = 0, rows*cols - 1 # index (pointers)

    # while left doesn't surpass right
    while left <= right:
        # index of center
        midInd = (left + right)//2 # index
        # center//cols gives row index, center%cols gives index of row row
        midEl = matrix[midInd//cols][midInd%cols] #value
        # true if target found, else, move pointers
        if midEl == target:
            return True
        elif midEl < target:
            left = midInd + 1
        else:
            right = midInd - 1
    return False

searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
