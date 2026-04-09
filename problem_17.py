def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price  # best day to buy
        elif price - min_price > max_profit:
            max_profit = price - min_price  # best profit

    return max_profit


# Example input
prices = [7, 1, 5, 3, 6, 4]

# Function call
result = maxProfit(prices)

# Output
print("Maximum Profit:", result)