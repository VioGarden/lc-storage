def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ans = []

    candidates.sort()
    lenlen = len(candidates)

    def helper(arr, count, index, n):

        if count > target:
            return
        if count == target:
            ans.append(arr[:])
            return
        prev = -1
        for elem in range(index, n):
            if candidates[elem] == prev:
                continue
            arr.append(candidates[elem])
            helper(arr, count + candidates[elem], elem + 1, n)
            arr.pop()
            prev = candidates[elem]
        
        return
    helper([], 0, 0, lenlen)
    return ans

