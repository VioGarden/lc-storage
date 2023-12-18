def twoSum(nums, target):
    prevMap = {}                        #dictionary initialization
    for i, n in enumerate(nums):        #index, value
        diff = target - n               #diff is target - value
        if diff in prevMap:             #if difference is found in dictionary
            return [prevMap[diff], i]   #return [index of dictionary, current index], end loop
        prevMap[n] = i                  #dict[value] = index

print(twoSum([2,7,11,15], 9))
# output : [0:1]