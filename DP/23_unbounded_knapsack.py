class Solution:
    def solve(self, idx, capacity, profit, weight):
        if idx == 0:
            if capacity >= weight[idx]:
                return profit[idx] * (capacity // weight[idx])
            else:
                return 0

        not_pick = self.solve(idx - 1, capacity, profit, weight)
        pick = 0
        if capacity >= weight[idx]:
            pick = profit[idx] + self.solve(idx, capacity - weight[idx], profit, weight)

        return max(pick, not_pick)


    def unboundedKnapsack(self, n, w, profit, weight):
        return self.solve(n-1, w, profit, weight)


class Solution:
    def solve(self, idx, capacity, profit, weight, dp):
        if idx == 0:
            if capacity >= weight[idx]:
                return profit[idx] * (capacity // weight[idx])
            else:
                return 0

        if dp[idx][capacity] != -1:
            return dp[idx][capacity]

        not_pick = self.solve(idx - 1, capacity, profit, weight, dp)
        pick = 0
        if capacity >= weight[idx]:
            pick = profit[idx] + self.solve(idx, capacity - weight[idx], profit, weight, dp)

        dp[idx][capacity] = max(pick, not_pick)

        return dp[idx][capacity]


    def unboundedKnapsack(self, n, w, profit, weight):
        dp = [[-1 for _ in range(w + 1)] for _ in range(n)]
        return self.solve(n-1, w, profit, weight, dp)
    

class Solution:
    def unboundedKnapsack(self, n, w, profit, weight):
        dp = [[0 for _ in range(w + 1)] for _ in range(n)]

        for capacity in range(w+1):
            if capacity >= weight[0]:
                dp[0][capacity] = profit[0] * (capacity // weight[0])

        for idx in range(1, n):
            for capacity in range(w + 1):
                not_pick = dp[idx - 1][capacity]
                pick = 0
                if capacity >= weight[idx]:
                    pick = profit[idx] + dp[idx][capacity - weight[idx]]

                dp[idx][capacity] = max(pick, not_pick)

        return dp[n-1][w]
    

class Solution:
    def unboundedKnapsack(self, n, w, profit, weight):
        prev = [0 for _ in range(w + 1)]
        curr = [0 for _ in range(w + 1)]

        for capacity in range(w+1):
            if capacity >= weight[0]:
                prev[capacity] = profit[0] * (capacity // weight[0])

        for idx in range(1, n):
            for capacity in range(w + 1):
                not_pick = prev[capacity]
                pick = 0
                if capacity >= weight[idx]:
                    pick = profit[idx] + curr[capacity - weight[idx]]

                curr[capacity] = max(pick, not_pick)
            prev = curr[:]

        return prev[w]