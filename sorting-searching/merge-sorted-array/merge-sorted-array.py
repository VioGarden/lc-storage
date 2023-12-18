def merge(nums1, m, nums2, n):
    point = len(nums1) - 1
    p1, p2 = m - 1, n - 1 # pointers because indeces are length - 1
    while point >= 0 and p2 >= 0 and p1 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[point] = nums2[p2]
            point -= 1
            p2 -= 1
        else:
            nums1[point], nums1[p1] = nums1[p1], nums1[point]
            point -= 1
            p1 -= 1
    while p2 >= 0: # scenario where p1 finishes but p2 still has smaller values
        nums1[point] = nums2[p2]
        point -= 1
        p2 -= 1
    return
    
print(merge([2,0], 1, [1], 1))