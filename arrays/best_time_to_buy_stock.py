def maxProfit(prices):
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        profit = max(profit, prices[i] - buy)

    return profit


class Solution(object):
    pass
