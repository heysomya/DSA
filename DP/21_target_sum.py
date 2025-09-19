from typing import List

# using dictionary
class Solution:
    def solve(self, idx, target, nums, dp):
        if idx == 0:
            if nums[0] == 0 and target == 0:
                return 2
            elif target == nums[idx] or target == -nums[idx]:
                return 1
            return 0
        
        if (idx, target) in dp:
            return dp[(idx, target)]

        add = self.solve(idx - 1, target - nums[idx], nums, dp)
        sub = self.solve(idx - 1, target + nums[idx], nums, dp)

        dp[(idx, target)] = add + sub
        return dp[(idx, target)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        return self.solve(n-1, target, nums, dp)


# using subset sum
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

        for idx in range(1, n):
            for target in range(k + 1):
                not_pick = dp[idx-1][target]
                pick = 0
                if target >= arr[idx]:
                    pick = dp[idx-1][target - arr[idx]]
                
                dp[idx][target] = (pick + not_pick)

        return dp[n-1][k]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        dp = [[0 for _ in range(totalSum + 1)] for _ in range(n)]
        
        self.countSubsetsWithSumK(nums, totalSum, dp)

        cnt = 0
        for s1 in range(totalSum + 1):
            s2 = totalSum - s1
            if s1 - s2 == target:
                cnt += dp[n-1][s1]

        return cnt
