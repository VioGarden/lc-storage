import math

def numFactoredBinaryTrees(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    n = len(arr)
    mod = 1000000007
    hashmap = {num : 1 for num in arr}
    for i in range(1, n):
        for j in range(i):
            quotient = arr[i] // arr[j]
            if quotient < 2 or math.sqrt(arr[i]) > arr[i - 1]:
                break
            if arr[i] % arr[j] == 0:
                hashmap[arr[i]] += hashmap[arr[j]] * hashmap.get(quotient, 0)
                hashmap[arr[i]] %= mod
    return sum(hashmap.values()) % mod