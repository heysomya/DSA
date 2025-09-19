class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, dp) -> int:
        m, n = len(text1), len(text2)

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if text1[idx1 - 1] == text2[idx2 - 1]:
                    dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1]
                else:
                    r1 = dp[idx1 - 1][idx2]
                    r2 = dp[idx1][idx2 - 1]
                    dp[idx1][idx2] = max(r1, r2)

        return dp[m][n]

    def printLCS(self, m, n, text1, text2):
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        self.longestCommonSubsequence(text1, text2, dp)

        res = []
        while m>0 and n>0:
            if text1[m-1] == text2[n-1]:
                res.append(text1[m-1])
                m-=1
                n-=1
            elif dp[m-1][n] > dp[m][n-1]:
                m-=1
            else:
                n-=1

        return "".join(reversed(res))