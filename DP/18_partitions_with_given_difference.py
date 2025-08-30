from typing import List

class Solution:
    def countSubsetsWithSumK(self, arr, k, dp):
        n = len(arr)

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


    def partitionWithGivenDifference(self, n, d, arr):
        total_sum = sum(arr)

        dp = [[0 for _ in range(total_sum + 1)] for _ in range(n)]
        self.countSubsetsWithSumK(arr, total_sum, dp)

        cnt = 0
        for s1 in range(total_sum, total_sum // 2 - 1, -1):
            s2 = total_sum - s1
            if s1 - s2 == d:
                cnt += dp[n-1][s1]
        
        return cnt