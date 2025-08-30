from typing import List

# Brute Force
class Solution:
    def solve(self, idx, target, arr):
        if idx == 0:
            if arr[idx] == 0 and target == 0:
                return 2
            elif target == 0 or target == arr[idx]:
                return 1
            else:
                return 0

        not_pick = self.solve(idx-1, target, arr)
        pick = 0
        if target >= arr[idx]:
            pick = self.solve(idx-1, target - arr[idx], arr)

        MOD = 10**9 + 7
        return (pick + not_pick) % MOD

    def countSubsetsWithSumK(self, arr, k):
        n = len(arr)

        return self.solve(n-1, k, arr)
    

# Memoization
class Solution:
    def solve(self, idx, target, arr, dp):
        if idx == 0:
            if arr[idx] == 0 and target == 0:
                return 2
            elif target == 0 or target == arr[idx]:
                return 1
            else:
                return 0

        if dp[idx][target] != -1:
            return dp[idx][target]

        not_pick = self.solve(idx-1, target, arr, dp)
        pick = 0
        if target >= arr[idx]:
            pick = self.solve(idx-1, target - arr[idx], arr, dp)
        
        MOD = 10**9 + 7
        dp[idx][target] = (pick + not_pick) % MOD
        
        return dp[idx][target]

    def countSubsetsWithSumK(self, arr, k):
        n = len(arr)
        dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

        return self.solve(n-1, k, arr, dp)


# Tabulation
class Solution:
    def countSubsetsWithSumK(self, arr, k):
        n = len(arr)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]

        # base case
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            if arr[0] <= k:
                dp[0][arr[0]] = 1

        MOD = 10**9 + 7
        for idx in range(1, n):
            for target in range(k + 1):
                not_pick = dp[idx-1][target]
                pick = 0
                if target >= arr[idx]:
                    pick = dp[idx-1][target - arr[idx]]
                
                dp[idx][target] = (pick + not_pick) % MOD

        return dp[n-1][k]
    

# Tabulation - 1D extra space
class Solution:
    def countSubsetsWithSumK(self, arr, k):
        n = len(arr)
        prev = [0 for _ in range(k+1)]
        curr = [0 for _ in range(k+1)]

        # base case
        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= k:
                prev[arr[0]] = 1

        MOD = 10**9 + 7
        for idx in range(1, n):
            for target in range(k + 1):
                not_pick = prev[target]
                pick = 0
                if target >= arr[idx]:
                    pick = prev[target - arr[idx]]
                
                curr[target] = (pick + not_pick) % MOD

            prev = curr[:]

        return prev[k]