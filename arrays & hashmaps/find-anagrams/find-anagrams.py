from collections import defaultdict
def find_anagrams(s, p):
    if len(p) > len(s): # edge case
        return []
    hashmap = defaultdict(int)
    final = []
    s_len = len(s)
    p_len = len(p)

    for letter in p: # make hashmap
        hashmap[letter] = 1 + hashmap.get(letter, 0)
    
    for i in range(p_len): # first check
        if s[i] in hashmap:
            hashmap[s[i]] -= 1
    
    if all(x == 0 for x in hashmap.values()): # if hashmap values are zero
        final.append(0)
    
    # add or subtract from hashmap
    for i in range(p_len, s_len):
        remove_index = i - p_len
        add_index = i
        if s[remove_index] in hashmap:
            hashmap[s[remove_index]] += 1
        if s[add_index] in hashmap:
            hashmap[s[add_index]] -= 1
        
        if all(x == 0 for x in hashmap.values()):
            final.append(remove_index + 1)
    return final



s = "abab"
p = "ab"
print(find_anagrams(s, p))


