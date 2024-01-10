def getLengthOfOptimalCompression(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    # i : index
    # k : how many left
    # prev : "" to init
    # prev_count : 1 to init

    cache = {}

    def count(index, k, prev_str, prev_cnt):
        if (index, k, prev_str, prev_cnt) in cache:
            return cache[(index, k, prev_str, prev_cnt)]
        if k < 0:
            return float('inf')
        if index == len(s):
            return 0
        # same previous letter
        if s[index] == prev_str:
            temp = 1 if prev_cnt in [1, 9, 99] else 0
            res = temp + count(index + 1, k, prev_str, prev_cnt + 1)

        # different previous letter
        else:
            res = min(
            count(index + 1, k - 1, prev_str, prev_cnt), # delete
            1 + count(index + 1, k, s[index], 1) # don't delete
        )
        cache[(index, k, prev_str, prev_cnt)] = res
        return res
        
    return count(0, k, "", 0)