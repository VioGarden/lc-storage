def characterReplacement(s, k):
    count = {}
    res = 0

    left = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0) # updating hashmap

        # (r - left + 1) = length of sliding window
        # while window is not valid
        # (r - left + 1) - max(count.values()) > k <-- sliding window is not valid
        while (r - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1 # decrement count of s[left] (left pointer)
            left += 1 # increment left pointer by one
        res = max(res, r - left + 1) # max of res and size of sliding window

    return res

# def characterReplacement(s, k):
#     count = {}
#     res = 0

#     left = 0
#     maxf = 0
#     for r in range(len(s)):
#         count[s[r]] = 1 + count.get(s[r], 0) # updating hashmap
#         maxf = max(maxf, count[s[r]])

#         if (r - left + 1) - maxf > k: # r - left + 1 <-- size of window
#             count[s[left]] -= left
#             left += 1

#         res = max(res, r - left + 1)
#     return res

        