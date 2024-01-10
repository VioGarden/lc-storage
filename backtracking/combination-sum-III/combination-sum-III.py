def combinationSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    ans = []
    arr = [1,2,3,4,5,6,7,8,9]
    def helper(curr, index, count, curr_len):
        if curr_len == k and count == n:
            ans.append(curr[:])
            return
        if curr_len > k or count > n:
            return
        for i in range(index, 9):
            curr.append(arr[i])
            helper(curr, i + 1, count + arr[i], curr_len + 1)
            curr.pop()
        return
        

    helper([], 0, 0, 0)
    return ans