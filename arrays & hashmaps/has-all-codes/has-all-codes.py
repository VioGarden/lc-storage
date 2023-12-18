def hasAllCodes(s, k):
    sss = set()
    for i in range(len(s) - k + 1):
        sss.add(s[i:i + k])
    if len(sss) == 2**k:
        return True
    return False