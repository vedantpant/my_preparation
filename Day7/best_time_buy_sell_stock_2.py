prices = [7,1,5,3,6,4]

def max_profit_2(prices):
    if not prices:
        return 0

    total_profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit = prices[i] - prices[i - 1]
            total_profit += profit

    return total_profit

print(max_profit_2(prices))