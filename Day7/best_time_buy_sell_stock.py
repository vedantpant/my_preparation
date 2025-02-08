prices = [7,1,5,3,6,4]


def find_max_profit(prices):
    l = 0
    r = 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            max_profit = max(max_profit, prices[r]- prices[r])
        else:
            l = r
        r += 1

    return max_profit


