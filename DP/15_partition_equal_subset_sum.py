from typing import List

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
        
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)

        if totalSum % 2 != 0: return False

        return self.subsetSumEqualsTarget(len(nums), totalSum // 2, nums)