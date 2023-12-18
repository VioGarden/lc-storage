def minimumReplacement(nums):
    ans = 0
    prev = nums[-1]
    for i in reversed(nums):
        if i > prev:
            times = (i + prev - 1) // prev
            prev = i // times
            ans += times - 1
        else:
            prev = i
    
    return ans


def minimumReplacement(nums):
    ans = 0
    prev = nums[-1]
    for i in reversed(nums):
        times = (i + prev - 1) // prev
        prev = i // times
        ans += times - 1
    
    return ans