def maxSumTwoNoOverlap(nums, firstLen, secondLen):
    prefix = [0]
    for i in nums:
        prefix.append(prefix[-1] + i)

    maxfirst = maxsecond = maxall = 0

    for k in range(secondLen, len(prefix) - firstLen):
        maxsecond = max(maxsecond, prefix[k] - prefix[k - secondLen])
        maxall = max(maxall, maxsecond + prefix[k + firstLen] - prefix[k])
    
    for j in range(firstLen, len(prefix) - secondLen):
        maxfirst = max(maxfirst, prefix[j] - prefix[j - firstLen])
        maxall = max(maxall, maxfirst + prefix[j + secondLen] - prefix[j])

    return maxall

