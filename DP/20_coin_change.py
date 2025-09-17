from typing import List

# Brute Force
class Solution:
    def solve(self, idx, target, coins):
        if idx == 0:
            if target % coins[idx] == 0:
                return target // coins[idx]
            else:
                return float('inf')

        not_pick = self.solve(idx - 1, target, coins)
        pick = float('inf')
        if target >= coins[idx]:
            pick = 1 + self.solve(idx, target - coins[idx], coins)

        return min(pick, not_pick)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        res = self.solve(n-1, amount, coins)

        if res == float('inf'):
            return -1
            
        return res


# Memoization
class Solution:
    def solve(self, idx, target, coins, dp):
        if idx == 0:
            if target % coins[idx] == 0:
                return target // coins[idx]
            else:
                return float('inf')

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_pick = self.solve(idx - 1, target, coins, dp)
        pick = float('inf')
        if target >= coins[idx]:
            pick = 1 + self.solve(idx, target - coins[idx], coins, dp)
        
        dp[idx][target] = min(pick, not_pick)
        return dp[idx][target]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        res = self.solve(n-1, amount, coins, dp)

        if res == float('inf'):
            return -1

        return res
    

# Tabulation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for _ in range(amount + 1)] for _ in range(n)]

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                dp[0][amt] = amt // coins[0]

        for idx in range(1, n):
            for target in range(amount + 1):
                not_pick = dp[idx - 1][target]
                pick = float('inf')
                if target >= coins[idx]:
                    pick = 1 + dp[idx][target - coins[idx]]
                
                dp[idx][target] = min(pick, not_pick)

        res = dp[n-1][amount]

        if res == float('inf'):
            return -1

        return res
    

# Tabulation with O(n) space
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        prev = [float('inf') for _ in range(amount + 1)] 
        curr = [float('inf') for _ in range(amount + 1)] 

        for amt in range(amount + 1):
            if amt % coins[0] == 0:
                prev[amt] = amt // coins[0]

        for idx in range(1, n):
            for target in range(amount + 1):
                not_pick = prev[target]
                pick = float('inf')
                if target >= coins[idx]:
                    pick = 1 + curr[target - coins[idx]]
                
                curr[target] = min(pick, not_pick)
            prev = curr[:]

        res = prev[amount]

        if res == float('inf'):
            return -1

        return res 