class Solution:
    def solve(self, idx1, idx2, text1, text2):
        if idx1 < 0 or idx2 < 0:
            return 0

        if text1[idx1] == text2[idx2]:
            return 1 + self.solve(idx1 - 1, idx2 - 1, text1, text2)
        else:
            r1 = self.solve(idx1 - 1, idx2, text1, text2)
            r2 = self.solve(idx1, idx2 - 1, text1, text2)
            return max(r1, r2) 

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        return self.solve(m-1, n-1, text1, text2)
    

class Solution:
    def solve(self, idx1, idx2, text1, text2, dp):
        if idx1 < 0 or idx2 < 0:
            return 0

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        if text1[idx1] == text2[idx2]:
            dp[idx1][idx2] = 1 + self.solve(idx1 - 1, idx2 - 1, text1, text2, dp)
            return dp[idx1][idx2]
        else:
            r1 = self.solve(idx1 - 1, idx2, text1, text2, dp)
            r2 = self.solve(idx1, idx2 - 1, text1, text2, dp)
            dp[idx1][idx2] = max(r1, r2)
            return dp[idx1][idx2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1, n-1, text1, text2, dp)
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1]
                else:
                    r1 = dp[idx1 - 1][idx2]
                    r2 = dp[idx1][idx2 - 1]
                    dp[idx1][idx2] = max(r1, r2)

        return dp[m][n]
    

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        prev = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    curr[idx2] = 1 + prev[idx2 - 1]
                else:
                    r1 = prev[idx2]
                    r2 = curr[idx2 - 1]
                    curr[idx2] = max(r1, r2)
            prev= curr[:]

        return prev[n]