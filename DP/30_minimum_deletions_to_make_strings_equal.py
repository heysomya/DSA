class Solution:
    def findLCS(self, text1, text2):
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

    def minDistance(self, word1: str, word2: str) -> int:
        x = self.findLCS(word1, word2)

        return len(word1) + len(word2) - 2*x