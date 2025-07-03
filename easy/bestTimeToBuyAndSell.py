class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  # Start with the highest possible value
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum buying price
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate and update max profit

        return max_profit
