class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)        # update lowest so far
            max_profit = max(max_profit, price - min_price)  # profit if sold today
        return max_profit
