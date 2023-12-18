def maxProfit(prices):
    if len(prices) < 1:
        return 0
    
    left, right = 0, 1 # left is buy, right is sell
    max_profit = 0 # max profit is 0
    while right < len(prices): # run loop while right pointer is in range
        if prices[left] < prices[right]: # if right value is higher than left value
            profit = prices[right] - prices[left] # profit for certain interval
            max_profit = max(max_profit, profit) # max is max of max and profit
        else: # if left value is higher than right
            left = right # shift left pointer all the way
        r += 1 # after every iteration, update right pointer by one
    return max_profit # return max profit
    