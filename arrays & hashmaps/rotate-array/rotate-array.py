def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]

# rotate([1,2,3,4,5,6,7], 3)

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    lenz = len(nums)
    k = k % lenz
    if k == 0:
        return nums
    nums += nums[:-k]
    del nums[:lenz-k]


def rotate(nums, k):
    for i in range(k):
        s = nums.pop(-1)
        nums.insert(0, s)

# (i + 2) % len(nums)