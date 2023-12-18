from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list)  #creates dictionary

    for i in strs:           #for each element in str
        count = [0] * 26     #count is an arrat of 26 0's

        for j in i:          #for each letter in dictionary
            count[ord(j) - ord("a")] += 1  #update count array where letter is found

        res[tuple(count)].append(i) #hash of each hashMap is a tuple of the list
        #use .append(i) instead of = i because multiple values per key
        #tuples can be hashes because they are immutable
        
    return res.values()  #return res will return the tuples, not values

# important, know that all values are in lowercase

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# output : [["bat"],["nat","tan"],["ate","eat","tea"]]