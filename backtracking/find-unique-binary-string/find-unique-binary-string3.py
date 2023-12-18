def findDifferentBinaryString(nums):
    def helper(curr, length, do_not_match_this_set):
        if len(curr) == length:
            if curr not in do_not_match_this_set:
                return curr
            return ""
        add_zero = helper(curr + "0", length, do_not_match_this_set)
        if add_zero:
            return add_zero
        return helper(curr + "1", length, do_not_match_this_set)
    n = len(nums)
    bset = set(nums)
    return helper("", n, bset)
