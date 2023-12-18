def isInterleave(s1, s2, s3):
    l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
    if l1+l2 != l3+1:
        return False
    pre = [True for _ in range(l2)]
    for j in range(1, l2):
        pre[j] = pre[j-1] and s2[j-1] == s3[j-1]
    for i in range(1, l1):
        cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
        for j in range(1, l2):
            cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
                     (pre[j] and s1[i-1] == s3[i+j-1])
        pre = cur[:]
    return pre[-1]

ss1 = "aabcc"
ss2 = "dbbca"
ss3 = "aadbbcbcac"

print(isInterleave(ss1, ss2, ss3))