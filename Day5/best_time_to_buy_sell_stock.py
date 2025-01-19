prices = [7, 10, 1, 3, 6, 9, 2]

def buy_sell_stocks(prices):

    left , right = 0, 1 # left is buy and right is sell
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

        else:
            left = right
        right += 1

    return max_profit
