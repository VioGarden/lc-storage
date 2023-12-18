def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)
    arr = [1] * n
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            arr[i] = arr[i - 1] + 1
    for j in range(n-2, -1, -1):
        if ratings[j] > ratings[j + 1]:
            arr[j] = max(arr[j], arr[j + 1] + 1)
    return sum(arr)

def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    n = len(ratings)
    if n == 1: return 1
    arr = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            if arr[i] <= arr[i - 1]:
                arr[i] = arr[i - 1] + 1
    for j in range(n - 2, 0, -1):
        if ratings[j] > ratings[j + 1]:
            if arr[j] <= arr[j + 1]:
                arr[j] = arr[j + 1] + 1
    if ratings[0] > ratings[1]:
        arr[0] = 1 + arr[1]
    if ratings[-1] > ratings[-2]:
        arr[-1] = 1 + arr[-2]
    return sum(arr)