def coinChange(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for c in coins:
        for i in range(c, amount + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[-1] == float('inf') else dp[-1]




import math

# Define a method called coinChange within the Solution class.
def coinChange(coins, amount):
    
    # Define a helper function for recursive calculations with memoization.
    def helper(rem, cache):
        # Base case: If the remaining amount is negative, it's not a valid solution.
        if rem < 0:
            return math.inf
        
        # Base case: If the remaining amount is zero, we have successfully covered it.
        if rem == 0:
            return 0
        
        # Check if the result for the current remaining amount is already cached.
        if rem in cache:
            return cache[rem]
        
        # Calculate the minimum number of coins needed for the current remaining amount.
        # Iterate over each coin denomination and recursively call helper with updated rem.
        # The +1 represents using one coin of the current denomination.
        cache[rem] = min(helper(rem - c, cache) + 1 for c in coins)
        
        # Store the result in the cache and return it.
        return cache[rem]
    
    # Initialize the calculation by calling the helper function with the target amount and an empty cache.
    ans = helper(amount, {})
    
    # Return the minimum number of coins needed or -1 if it's not possible to make up the amount.
    return -1 if ans == math.inf else ans
