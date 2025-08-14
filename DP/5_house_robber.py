from typing import List


# Brute Force
class Solution:
    def solve(self, nums, idx):
        if idx == 0: return nums[idx]

        if idx < 0: return 0

        pick = nums[idx] + self.solve(nums, idx - 2)
        notPick = self.solve(nums, idx - 1)

        return max(pick, notPick)


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.solve(nums, n-1)


# Memoization
class Solution2:
    def solve(self, nums, idx, dp):
        if idx == 0: return nums[idx]
        if idx < 0: return 0

        if dp[idx] != -1:
            return dp[idx]

        pick = nums[idx] + self.solve(nums, idx - 2, dp)
        notPick = self.solve(nums, idx - 1, dp)

        dp[idx] = max(pick, notPick)
        return dp[idx]


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        return self.solve(nums, n-1, dp)


# Tabulation
class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]

        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for idx in range(2, n):
            pick = nums[idx] + dp[idx - 2]
            notPick = dp[idx - 1]
            dp[idx] = max(pick, notPick)

        return dp[n-1]


# Tabulation - Constant Space
class Solution4:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for idx in range(2, n):
            pick = nums[idx] + prev2
            notPick = prev
            curr = max(pick, notPick)
            prev2, prev = prev, curr

        return prev


def main():
    numsArr = [[1,2,3,1], [2,7,9,3,1]]

    for nums in numsArr:
        s = Solution4()
        res = s.rob(nums)
        print(res)

main()
