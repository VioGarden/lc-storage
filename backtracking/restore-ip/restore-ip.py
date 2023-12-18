def restoreIpAddresses(s):
    final = []
    def backtrack(string, current, count):
        if count == 4:
            if not string:
                final.append(current[:-1])
            return
        for i in range(1, 4):
            if i > len(string):
                continue
            if i > 1 and string[0] == '0':
                continue
            if i > 2 and int(string[:3]) > 255:
                continue
            backtrack(string[i:], current + string[:i]+ ".", count + 1)
    
    backtrack(s, "", 0)
    return final

s = "25525511135"
print(restoreIpAddresses(s))