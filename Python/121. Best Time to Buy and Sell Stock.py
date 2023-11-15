class Solution:  # Works but too slow
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0

        while i < len(prices):
            j = i + 1
            while j < len(prices):
                spread = prices[j] - prices[i]
                if spread > profit:
                    profit = spread
                j += 1

            i += 1

        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Update the min_price if a new lower price is found
            min_price = min(min_price, price)

            # Calculate profit if the stock were sold at the current price
            profit = price - min_price

            # Update max_profit if the current profit is greater than the previous max
            max_profit = max(max_profit, profit)

        return max_profit
