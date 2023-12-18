def minDeletions(s):
    table = {}
    for i in s:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1
            
    res = 0
    used = set() # for checking that we only hvae unique values 
    for k,v in table.items():
        while v > 0 and v in used:
            v -= 1
            res += 1
        used.add(v)
    return res