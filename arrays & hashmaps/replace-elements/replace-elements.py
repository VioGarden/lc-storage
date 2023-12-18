def replaceElements(arr):
    if len(arr) == 1:
        return [-1]
    
    final = [-1]
    curr_max = arr[-1]
    i = len(arr) - 1
    while i > 0:
        curr_max = max(curr_max, arr[i])
        final.append(curr_max)
        i -= 1
    
    left, right = 0, len(final) - 1
    while left < right:
        final[left], final[right] = final[right], final[left]
        left += 1
        right -= 1
    
    return final


arr = [17,18,5,4,6,1]
print(replaceElements(arr))

def replaceElements(arr):
    if len(arr) == 1:
        return [-1]
    highest = -1
    for i in range(len(arr) - 1, -1, -1):
        hold = arr[i]
        arr[i] = highest
        highest = max(hold, highest)
    return arr
