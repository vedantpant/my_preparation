prices = [7, 5, 1, 3, 9, 5]


def max_profit(prices):
    left, right = 0, 1  # left = buy, right = sell

    maxP = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
        else:
            left = right
        right += 1

    return maxP

print(max_profit(prices))
