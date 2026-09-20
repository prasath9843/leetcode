class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0

        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i - 1])
                       for i in range(1, len(prices)))

        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k]