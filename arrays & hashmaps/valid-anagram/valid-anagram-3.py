from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)
            
#76 ms
#14 MB