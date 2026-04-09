class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(current):
            rem = amount-current
            if rem in dp:
                return dp[rem]
                
            if rem < 0: 
                return float("inf")
            if rem == 0:
                return 0

            least = float("inf")
            for i in range(len(coins)):
                least = min(1 + dfs(current + coins[i]), least)
            
            dp[rem] = least
            return least

        result = dfs(0)
        return result if result < float("inf") else -1
        


