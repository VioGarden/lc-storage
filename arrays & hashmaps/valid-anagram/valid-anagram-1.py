def isAnagram(s, t): 
    if len(s) != len(t):                        #if lengths are different, cannot be anagram
        return False                            #return false

    countS, countT = {}, {}                     #initialize two dictionaries

    for i in range(len(s)):                     #for i in range of length of an anagram
        countS[s[i]] = 1 + countS.get(s[i], 0)  #dict[value(letter in anagram s)] = number_of_occurances
        countT[t[i]] = 1 + countT.get(t[i], 0)  #dict[value(letter in anagram t)] = number_of_occurances
    
    for c in countS:                            #for c in length of hashDict
        if countS[c] != countT.get(c, 0):       #if value for key of countS != value for key of countT
            return False                        #return False
        
    return True                #no problems, return True, are anagrams

#51 ms
#15.3 MB

print(isAnagram("anagram", "nagaram"))
# output : True