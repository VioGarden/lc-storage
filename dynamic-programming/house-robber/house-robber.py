# get sub problems
# rob = max(arr[0] + rob[2:n], rob[1:n] )
# use of max, only need to look at previous 2
# [rob1, rob2, n, n + 1]
def rob(nums):
    rob1, rob2 = 0, 0 
    for n in nums:
        temp = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2