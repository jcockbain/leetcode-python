def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


def maxProfit_2(prices):
    min_price = sys.maxint
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif (prices[i] - min_price > max_profit):
            max_profit = prices[i] - min_price
    return max_profit


print(maxProfit([1, 2, 5, 3, 7, 1]))
