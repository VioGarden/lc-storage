def nextGreatestLetter(letters, target):
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right)//2

        if target >= letters[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return letters[left]

