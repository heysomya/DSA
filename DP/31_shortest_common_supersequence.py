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

        return dp

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = self.longestCommonSubsequence(str1, str2)
        m, n = len(str1), len(str2)
        res = []
    
        while m>0 and n>0:
            if str1[m-1] == str2[n-1]:
                res.append(str1[m-1])
                m-=1
                n-=1
            else:
                if dp[m-1][n] >= dp[m][n-1]:
                    res.append(str1[m-1])
                    m-=1
                else:
                    res.append(str2[n-1])
                    n-=1

        # add leftover elements
        while m>0:
            res.append(str1[m-1])
            m-=1
                
        while n>0:
            res.append(str2[n-1])
            n-=1
                

        return "".join(reversed(res))