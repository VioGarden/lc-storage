def topKFrequent(nums, k):
    #hashmap | element | number of occurances |  O(n)
    #bucketsort | number of occurances | element |   O(n)
    #iterate backwards through the bucketsort to find the k most frequent  O(n)
    
    hashMap = {}                                    #hashmap initialization
    bucket = [[] for i in range(len(nums) + 1)]     #bucket initialization
    
    for i in nums:                                  #loop over nums and add to hashmap
        hashMap[i] = 1 + hashMap.get(i,0)
        
    for key, value in hashMap.items():              #for each value in hashmap, add to bucket
        bucket[value].append(key)
        
    output = []                                     #initialize output list
    for i in range(len(bucket) - 1, -1, -1):         #for loop where i descends from array length -1
        for j in bucket[i]:                         #for loop where j is elements of each list in bucket list
            output.append(j)                        #if element is inside, append to output list
            if len(output) == k:                    #when length of output list is k, return
                return output

print(topKFrequent([1,1,1,2,2,3], 2))
# output : [1,2]