class Solution:
    def solve(self, idx, weight, values, weights):
        if idx == 0:
            if weights[idx] <= weight:
                return values[idx]
            else:
                return 0

        
        not_pick = self.solve(idx - 1, weight, values, weights)
        pick = 0
        if weight >= weights[idx]:
            pick = values[idx] + self.solve(idx - 1, weight - weights[idx], values, weights)

        return max(pick, not_pick)

    def knapsack(self, values, weights, n, w):
        return self.solve(n-1, w, values, weights)


class Solution:
    def solve(self, idx, weight, values, weights, dp):
        if idx == 0:
            if weights[idx] <= weight:
                return values[idx]
            else:
                return 0

        if dp[idx][weight] != -1:
            return dp[idx][weight]
            
        not_pick = self.solve(idx - 1, weight, values, weights, dp)
        pick = 0
        if weight >= weights[idx]:
            pick = values[idx] + self.solve(idx - 1, weight - weights[idx], values, weights, dp)

        dp[idx][weight] = max(pick, not_pick)

        return dp[idx][weight]

    def knapsack(self, values, weights, n, w):
        dp = [[-1 for _ in range(w + 1)] for _ in range(n)]
        return self.solve(n-1, w, values, weights, dp)


class Solution:
    def knapsack(self, values, weights, n, w):
        dp = [[0 for _ in range(w + 1)] for _ in range(n)]

        # base case
        for weight in range(w+1):
            if weight >= weights[0]:
                dp[0][weight] = values[0]

        for idx in range(1, n):
            for weight in range(w + 1):
                not_pick = dp[idx - 1][weight]
                pick = 0
                if weight >= weights[idx]:
                    pick = values[idx] + dp[idx - 1][weight - weights[idx]]
                dp[idx][weight] = max(pick, not_pick)

        return dp[n-1][w]


class Solution:
    def knapsack(self, values, weights, n, w):
        dp = [[0 for _ in range(w + 1)] for _ in range(n)]

        prev = [0 for _ in range(w+1)]
        curr = [0 for _ in range(w+1)]

        # base case
        for weight in range(w+1):
            if weight >= weights[0]:
                prev[weight] = values[0]

        for idx in range(1, n):
            for weight in range(w + 1):
                not_pick = prev[weight]
                pick = 0
                if weight >= weights[idx]:
                    pick = values[idx] + prev[weight - weights[idx]]
                curr[weight] = max(pick, not_pick)
            
            prev = curr[:]

        return prev[w]