def sortColors(nums):
    hashmap = {}
    for i in nums:
        hashmap[i] = 1 + hashmap.get(i, 0)

    for j in range(len(nums)):
        """"""
        
    return

sortColors([2,1,0,2,1,0])