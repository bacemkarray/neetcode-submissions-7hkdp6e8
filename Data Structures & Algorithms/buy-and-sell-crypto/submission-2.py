class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        b, s = 0, 1

        while s < len(prices):
            profit = prices[s] - prices[b]
            if profit < 0:
                b = s
            else:
                max_profit = max(max_profit, profit)
            s += 1
        
        return max_profit