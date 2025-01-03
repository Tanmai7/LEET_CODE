# def maxProfit(prices):
#     min_price = float('inf')  # Initially set to a large number
#     max_profit = 0  # Initially set to 0 since no profit is made yet
#     for price in prices:
#         # Update the minimum price encountered so far
#         if price < min_price:
#             min_price = price
#         # Calculate the profit if we sell on the current day
#         profit = price - min_price
#         # Update the maximum profit if this profit is higher
#         if profit > max_profit:
#             max_profit = profit
#     return max_profit

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price
        # Calculate the profit if we sell on the current day
        profit = price - min_price
        # Update the maximum profit if this profit is higher
        if profit > max_profit:
            max_profit = profit
            
    return max_profit

# Input: Take the stock prices as input from the user
prices = list(map(int, input("Enter the stock prices separated by spaces: ").split()))

# Output: Display the maximum profit
print("Maximum profit:", maxProfit(prices))
