def kthGrammar(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    if n == 1:
        return 0
    half = 2**(n - 2)
    if k > half:
        return 1 if self.kthGrammar(n - 1, k - half) == 0 else 0
    else:
        return self.kthGrammar(n - 1, k)