# if sorted, use pointers

def intersect(nums1, nums2):
    i, j = 0, 0 # initialize pointers
    output = [] # output array
    nums1, nums2, = sorted(nums1), sorted(nums2) # scenario of sorted numbers
    while i < len(nums1) and j < len(nums2): # while both pointers haven't reached the end
        if nums1[i] < nums2[j]: # if nums2 is bigger, try to make i catch up
            i += 1
        elif nums1[i] > nums2[j]: # if nums1 is bigger, try to make j catch up
            j += 1
        else:
            output.append(nums1[i]) # only append if the nums are the same
            i += 1 # increment both by one
            j += 1
    return output

# know that when one array pointer reaches the end, intersection cannot happen anymore