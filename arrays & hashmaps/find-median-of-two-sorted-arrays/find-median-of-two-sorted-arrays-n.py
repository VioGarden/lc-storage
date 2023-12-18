from collections import deque

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    arr = []
    n1, n2 = deque(nums1), deque(nums2)
    while n1 and n2:
        if n1[0] < n2[0]:
            arr.append(deque.popleft(n1))
        else:
            arr.append(deque.popleft(n2))
    while n1:
        arr.append(deque.popleft(n1))
    while n2:
        arr.append(deque.popleft(n2))
    if not arr:
        return 0
    if len(arr) % 2 == 1:
        return arr[len(arr)//2]
    else:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1])/2.0


    
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums1 = deque(nums1)
    nums2 = deque(nums2)
    n1, n2, n1count, n2count = len(nums1), len(nums2), 0, 0
    if not (n1 + n2):
        return 0
    elif not n1:
        nums1 = nums2
    elif not n2:
        pass
    else:
        for _ in range(n1 + n2):
            if nums1[0] < nums2[0]:
                nums1.append(nums1.popleft())
                n1count += 1
                if n1count == n1:
                    for _ in range(n2 - n2count):
                        nums1.append(nums2.popleft())
                    break
            else:
                nums1.append(nums2.popleft())
                n2count += 1
                if n2count == n2:
                    for _ in range(n1 - n1count):
                        nums1.append(nums1.popleft())
                    break
    
    if (n1+n2)%2 == 1:
        return nums1[(n1+n2)//2]
    else:
        return (nums1[(n1+n2)//2] + nums1[(n1+n2)//2 - 1])/2.0

