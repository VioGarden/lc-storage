from collections import deque

def lengthOfLongestSubstring(s):
    empty = []
    longest = 0
    d = deque(empty)
    for i in s:
        if i in d:
            while i in d:
                deque.popleft(d)
        d.append(i)
        longest = max(len(d), longest)
    return longest