def maximumCandies(candies, k):
    n = len(candies)
    left = 1  
    right = max(candies)  
    final = 0 
    while left <= right:   # <=
        pile_count = 0 # number of piles we can make
        mid = (left) + (right - left) // 2   # mid point finding way (mid is number of candy per pile)
        for i in range(n): 
            pile_count += candies[i] // mid # how many piles can we make
        if pile_count >= k: # if piles made (with a certain value for amount of candy per pile) exceeds children
            final = max(final, mid)   # set final to mid (number of candy per pile)
            left = mid + 1   
        else: 
            right = mid - 1   
    return final

print(maximumCandies([72], 3))