def longestConsecutive(nums):
    numSet = set(nums)                      #turn into set
    longest = 0                             #initialize output
    
    for i in numSet:                        #iterate over numSet
        if (i - 1) not in numSet:           #if i is that start of a chain
            length = 1                      #initialize length to 1
            while (i + length) in numSet:   #while chain continues
                length += 1                 #update length
            if length > longest:            #if length is longest chain
                longest = length            #update output
            #longest = max(length, longest)
                
    return longest                          #return output
    
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# output : 9