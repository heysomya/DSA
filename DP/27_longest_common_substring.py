from typing import List

# Leetcode 718: Maximum Length of an Repeated Subarray
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        maxi = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    maxi = max(maxi, dp[i][j])

        return maxi