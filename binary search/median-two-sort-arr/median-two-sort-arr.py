def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2) 
    half = total // 2 # index of median if arrays were 1
    if len(B) < len(A): # want to make the shorter array A
        A, B = B, A

    left, right = 0, len(A) - 1 # pointers for array 1
    while True:
        i = (left + right) // 2 # halfway point of index a (floor)
        j = half - i - 2 # halfway point for index of b

        Aleft = A[i] if i >= 0 else float("-infinity") # value of A left
        Aright = A[i + 1] if (i + 1) < len(A) else float("infinity") # value of A right
        Bleft = B[j] if j >= 0 else float("-infinity") # value of B left
        Bright = B[j + 1] if (j + 1) < len(B) else float("infinity") # value of B right

        # if the right most of both arrays are greater than each others lefts, found right place
        if Aleft <= Bright and Bleft <= Aright: 
            # odd
            if total % 2: # if length is an odd number 
                return min(Aright, Bright) # return the smaller one cause that will be the median
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # max of left and min of right / 2 (could get float)
        elif Aleft > Bright:
            right = i - 1 # if the left most of A is greater than B right, A is too big
        else: # if Bleft is greater than Right, A is too small
            left = i + 1