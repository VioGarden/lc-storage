from collections import Counter

def intersect(nums1, nums2):
    c = Counter(nums1) # Counter automatically creates a hashmap, list value : num of occurances
    output = [] # output array
    for n in nums2: # iterate over second array
        if c[n] > 0: # if the number exists in the nums1 hashmap
            output.append(n) # append to the output list
            c[n] -= 1 # subtract one from the nums1 hashmap
    return output

print(intersect([1,2,3,4,5,6], [4,5,6,7,8,9]))