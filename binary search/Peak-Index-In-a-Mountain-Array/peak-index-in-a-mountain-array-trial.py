def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    if arr[left] > arr[left + 1]:
        return 0
    if arr[right] > arr[right - 1]:
        return right
    while left < right:
        mid = (left + right)//2
        if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
            return mid
        elif arr[mid + 1] < arr[mid]:
            right = mid
        else:
            left = mid + 1
    return left
