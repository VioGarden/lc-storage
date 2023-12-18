from collections import defaultdict

def groupThePeople(groupSizes):
    hashmap = defaultdict(list)
    for i in range(len(groupSizes)):
        hashmap[groupSizes[i]].append(i)
    ans = []
    for size, index in hashmap.items():
        for count in range(len(index)//size):            
            temp = []
            i = 0
            while i < size:
                temp.append(index[i])
                i += 1
            ans.append(temp)
    return ans
