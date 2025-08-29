class Solution:
    def subsetWithSumK(self, n, arr, target, dp):
        # base cases
        dp[0][arr[0]] = True
        for i in range(n): dp[i][0] = True

        for idx in range(1, n):
            for tar in range(target + 1):
                not_pick = dp[idx - 1][tar]
                pick = False
                if tar >= arr[idx]: pick = dp[idx - 1][tar - arr[idx]]
                dp[idx][tar] = pick or not_pick
        
        return dp[n-1][target]

    def minSubsetDiff(self, arr, n):
        total_sum = sum(arr)
        dp = [[False for _ in range(total_sum + 1)] for _ in range(n)]
        
        self.subsetWithSumK(n, arr, total_sum, dp)
        
        mini = float('inf')
        for target in range(total_sum + 1):
            if dp[n-1][target]:
                s1 = target
                s2 = total_sum - target
                mini = min(mini, abs(s2 - s1))
        
        return mini