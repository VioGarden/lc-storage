def countAndSay(n):
    ans = "1"
    for i in range(n - 1):
        count = 1
        temp = []
        for j in range(1, len(ans)):
            if ans[j] == ans[j - 1]:
                count += 1
            else:
                temp.append(str(count))
                temp.append(ans[j - 1])
                count = 1
        temp.append(str(count))
        temp.append(ans[-1])
        ans = "".join(temp)
    return ans