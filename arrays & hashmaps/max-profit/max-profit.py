def maxProfit(prices):
    profit = 0 # initial profit
    for i in range(1, len(prices)): # looping through everything but first element
        if prices[i] > prices[i - 1]: # every i, compare to previous position, if current > past
            profit += (prices[i] - prices[i - 1]) # profit is possible, so profit of that margin
    return profit # return profit