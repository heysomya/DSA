from typing import List

# Brute Force
class Solution:
    def solve(self, idx, can_buy, transactions_left, prices, n):
        if idx == n:
            return 0
        
        profit = 0
        if transactions_left > 0:
            if can_buy:
                buy = -prices[idx] + self.solve(idx + 1, 0, transactions_left, prices, n)
                not_buy = self.solve(idx + 1, 1, transactions_left, prices, n)
                profit = max(buy, not_buy)
            else:
                sell = prices[idx] + self.solve(idx + 1, 1, transactions_left - 1, prices, n)
                not_sell = self.solve(idx + 1, 0, transactions_left, prices, n)
                profit = max(sell, not_sell)
            
        return profit


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return self.solve(0, 1, 2, prices, n)
    

# Memoization
class Solution:
    def solve(self, idx, can_buy, transactions_left, prices, n, dp):
        if idx == n:
            return 0
        
        if dp[idx][can_buy][transactions_left] != -1:
            return dp[idx][can_buy][transactions_left]

        profit = 0
        if transactions_left > 0:
            if can_buy:
                buy = -prices[idx] + self.solve(idx + 1, 0, transactions_left, prices, n, dp)
                not_buy = self.solve(idx + 1, 1, transactions_left, prices, n, dp)
                profit = max(buy, not_buy)
            else:
                sell = prices[idx] + self.solve(idx + 1, 1, transactions_left - 1, prices, n, dp)
                not_sell = self.solve(idx + 1, 0, transactions_left, prices, n, dp)
                profit = max(sell, not_sell)

        dp[idx][can_buy][transactions_left] = profit

        return profit


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return self.solve(0, 1, 2, prices, n, dp)
    

# Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        for idx in range(n-1, -1, -1):
            for can_buy in range(2):
                for transactions_left in range(1, 3):
                    profit = 0
                    if can_buy:
                        buy = -prices[idx] + dp[idx + 1][0][transactions_left]
                        not_buy = dp[idx + 1][1][transactions_left]
                        profit = max(buy, not_buy)
                    else:
                        sell = prices[idx] + dp[idx + 1][1][transactions_left - 1]
                        not_sell = dp[idx + 1][0][transactions_left]
                        profit = max(sell, not_sell)

                    dp[idx][can_buy][transactions_left] = profit

        return dp[0][1][2]