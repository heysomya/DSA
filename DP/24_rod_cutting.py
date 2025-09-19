# Brute Force
class Solution:
    def solve(self, idx, capacity, price):
        if idx == 0:
            if capacity > idx:
                return capacity * price[0]
            else:
                return 0

        not_pick = self.solve(idx - 1, capacity, price)
        pick = -1
        if capacity > idx:
            pick = price[idx] + self.solve(idx, capacity - (idx + 1), price)

        return max(pick, not_pick)

    def cutRod(self, n, price):
        return self.solve(n - 1, n, price)
    

# Memoization
class Solution:
    def solve(self, idx, capacity, price, dp):
        if idx == 0:
            if capacity > idx:
                return capacity * price[0]
            else:
                return 0

        if dp[idx][capacity] != -1:
            return dp[idx][capacity]

        not_pick = self.solve(idx - 1, capacity, price, dp)
        pick = -1
        if capacity > idx:
            pick = price[idx] + self.solve(idx, capacity - (idx + 1), price, dp)

        dp[idx][capacity] = max(pick, not_pick)

        return dp[idx][capacity]

    def cutRod(self, n, price):
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.solve(n - 1, n, price, dp)
    

# Tabulation
class Solution:
    def cutRod(self, n, price):
        dp = [[0 for _ in range(n+1)] for _ in range(n)]

        for capacity in range(1, n+1):
            dp[0][capacity] = capacity * price[0]

        for idx in range(1, n):
            for capacity in range(n+1):
                not_pick = dp[idx - 1][capacity]
                pick = -1
                if capacity > idx:
                    pick = price[idx] + dp[idx][capacity - (idx + 1)]

                dp[idx][capacity] = max(pick, not_pick)

        return dp[n-1][n]
    

# Tabulation Space Optimised
class Solution:
    def cutRod(self, n, price):
        prev = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]

        for capacity in range(1, n+1):
            prev[capacity] = capacity * price[0]

        for idx in range(1, n):
            for capacity in range(n+1):
                not_pick = prev[capacity]
                pick = -1
                if capacity > idx:
                    pick = price[idx] + curr[capacity - (idx + 1)]

                curr[capacity] = max(pick, not_pick)
            prev = curr[:]

        return prev[n]