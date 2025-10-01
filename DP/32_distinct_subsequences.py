# Recursion
class Solution:
    def solve(self, idx1, idx2, s, t):
        if idx2 < 0:
            return 1
        
        if idx1 < 0:
            return 0

        f = 0
        if s[idx1] == t[idx2]:
            f += self.solve(idx1 - 1, idx2 - 1, s, t)
            f += self.solve(idx1 - 1, idx2, s, t)
        else:
            f += self.solve(idx1 - 1, idx2, s, t)

        return f
        
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        return self.solve(m-1, n-1, s, t)
    

# Memoization
class Solution:
    def solve(self, idx1, idx2, s, t, dp):
        if idx2 < 0:
            return 1
        
        if idx1 < 0:
            return 0

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        f = 0
        if s[idx1] == t[idx2]:
            f += self.solve(idx1 - 1, idx2 - 1, s, t, dp)
            f += self.solve(idx1 - 1, idx2, s, t, dp)
        else:
            f += self.solve(idx1 - 1, idx2, s, t, dp)


        dp[idx1][idx2] = f

        return dp[idx1][idx2]
        
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solve(m-1, n-1, s, t, dp)
    

# Tabulation
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # base case
        for idx1 in range(m):
            dp[idx1][0] = 1

        for idx1 in range(1, m + 1):
            for idx2 in range(1, n + 1):
                if s[idx1 - 1] == t[idx2 - 1]:
                    dp[idx1][idx2] += dp[idx1 - 1][idx2 - 1]
                    dp[idx1][idx2] += dp[idx1 - 1][idx2]
                else:
                    dp[idx1][idx2] += dp[idx1 - 1][idx2]

        return dp[m][n]
    

# Tabulation (Space Optimized)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        prev = [0 for _ in range(n+1)]
        curr = [0 for _ in range(n+1)]

        # base case
        prev[0] = 1

        for idx1 in range(1, m+1):
            curr[0] = 1
            for idx2 in range(1, n+1):
                if s[idx1 - 1] == t[idx2 - 1]:
                    curr[idx2] = prev[idx2 - 1] + prev[idx2]
                else:
                    curr[idx2] = prev[idx2]
            prev = curr[:]

        return prev[n]
