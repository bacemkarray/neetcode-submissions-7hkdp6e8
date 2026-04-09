class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # cache = {}
        # def dfs(current):
        #     if current in cache:
        #         return cache[current]
                
        #     least = float("inf")
        #     if current == 0:
        #         return 0
        #     if current >= 0:
        #         for c in coins:
        #             least = min(1 + dfs(current - c), least)
            
        #     cache[current] = least
        #     return least


        # result = dfs(amount)
        # return result if result < float("inf") else -1
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])

        
        return dp[amount] if dp[amount] < amount+1 else -1
        