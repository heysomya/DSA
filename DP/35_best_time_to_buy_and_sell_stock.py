from typing import List

# Brute Force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0

        for i in range(n-1):
            for j in range(i+1, n):
                maxi = max(maxi, prices[j] - prices[i])

        return maxi
    
# Optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        maxi = 0
        mini = prices[0]

        for i in range(1, n):
            maxi = max(maxi, prices[i] - mini)
            mini = min(mini, prices[i])

        return maxi