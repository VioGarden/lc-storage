def isAnagram(s, t):
    if len(s) != len(t):
        return False
    arr = []
    for i in s:
        arr.append(i)
    for i in t:
        if i in arr:
            arr.remove(i)
    if len(arr) == 0:
        return True
    return False

#2363 ms
#14.8 MB
            