from typing import List

# Brute Force
class Solution:
    def solve(self, idx, target, coins):
        if idx == 0:
            if target % coins[idx] == 0:
                return 1
            return 0

        not_pick = self.solve(idx-1, target, coins)
        pick = 0
        if target >= coins[idx]:
            pick = self.solve(idx, target - coins[idx], coins)

        return pick + not_pick
         
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        return self.solve(n-1, amount, coins)
    

# Memoization
class Solution:
    def solve(self, idx, target, coins, dp):
        if idx == 0:
            if target % coins[idx] == 0:
                return 1
            return 0

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_pick = self.solve(idx-1, target, coins, dp)
        pick = 0
        if target >= coins[idx]:
            pick = self.solve(idx, target - coins[idx], coins, dp)
        
        dp[idx][target] = pick + not_pick
        return dp[idx][target]
         
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        return self.solve(n-1, amount, coins, dp)
    

# Tabulation 
class Solution:         
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]

        # base case 
        for target in range(amount + 1):
            if target % coins[0] == 0:
                dp[0][target] = 1

        for idx in range(1, n):
            for target in range(amount + 1):
                not_pick = dp[idx-1][target]
                pick = 0
                if target >= coins[idx]:
                    pick = dp[idx][target - coins[idx]]
                
                dp[idx][target] = pick + not_pick

        return dp[n-1][target]
    

# tabulation Space Optimised
class Solution:         
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        prev = [0 for _ in range(amount + 1)]
        curr = [0 for _ in range(amount + 1)]

        # base case 
        for target in range(amount + 1):
            if target % coins[0] == 0:
                prev[target] = 1

        for idx in range(1, n):
            for target in range(amount + 1):
                not_pick = prev[target]
                pick = 0
                if target >= coins[idx]:
                    pick = curr[target - coins[idx]]
                
                curr[target] = pick + not_pick
            prev = curr[:]

        return prev[target]