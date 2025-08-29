# Brute Force
class Solution:
    def solve(self, idx, target, arr):
        if idx == 0:
            if target == 0: return True
            
            return arr[idx] == target

        not_pick = self.solve(idx - 1, target, arr)
        pick = False
        if target >= arr[idx]:
            pick = self.solve(idx - 1, target - arr[idx], arr)

        return pick or not_pick

    def subsetSumEqualsTarget(self, n, target, arr):
        return self.solve(n-1, target, arr)


# Memoization
class Solution:
    def solve(self, idx, target, arr, dp):
        if idx == 0:
            if target == 0: return True
            return arr[idx] == target

        if dp[idx][target] != -1: return dp[idx][target]

        not_pick = self.solve(idx - 1, target, arr, dp)
        pick = False
        if target >= arr[idx]:
            pick = self.solve(idx - 1, target - arr[idx], arr, dp)

        dp[idx][target] = pick or not_pick
        return dp[idx][target]

    def subsetSumEqualsTarget(self, n, target, arr):
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        return self.solve(n-1, target, arr, dp)


# Tabulation
class Solution:
    def subsetSumEqualsTarget(self, n, k, arr):
        dp = [[False for _ in range(k + 1)] for _ in range(n)]

        dp[0][0] = True
        if arr[0] <= k: dp[0][arr[0]] = True

        for idx in range(1, n):
            for target in range(k+1):
                not_pick = dp[idx - 1][target]
                pick = False
                if target >= arr[idx]:
                    pick = dp[idx - 1][target - arr[idx]]

                dp[idx][target] = pick or not_pick

        return dp[n-1][target]


# Tabulation - O(N) extra space
class Solution:
    def subsetSumEqualsTarget(self, n, k, arr):
        prev = [False for _ in range(k+1)]

        prev[0] = True
        if arr[0] <= k: prev[arr[0]] = True

        for idx in range(1, n):
            curr = [False for _ in range(k+1)]
            for target in range(k+1):
                not_pick = prev[target]
                pick = False
                if target >= arr[idx]:
                    pick = prev[target - arr[idx]]

                curr[target] = pick or not_pick
            prev = curr

        return prev[k]
