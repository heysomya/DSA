# Brute Force
class Solution:
    def solve(self, idx1, idx2, s, p):
        if idx1==0 and idx2==0:
            return True

        if idx2==0 and idx1 > 0:
            return False
        
        if idx1==0 and idx2 > 0:
            while idx2 > 0:
                if p[idx2 - 1] != '*':
                    return False
                idx2 -= 1
            return True

        if s[idx1 - 1] == p[idx2 - 1] or p[idx2 - 1] == '?':
            return self.solve(idx1 - 1, idx2 - 1, s, p)
        elif p[idx2 - 1] == '*':
            return self.solve(idx1 - 1, idx2, s, p) or self.solve(idx1, idx2 - 1, s, p)
        else:
            return False

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        return self.solve(m, n, s, p)
    

# Memoization
class Solution:
    def solve(self, idx1, idx2, s, p, dp):
        if idx1==0 and idx2==0:
            return True

        if idx2==0 and idx1 > 0:
            return False
        
        if idx1==0 and idx2 > 0:
            while idx2 > 0:
                if p[idx2 - 1] != '*':
                    return False
                idx2 -= 1
            return True

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]

        if s[idx1 - 1] == p[idx2 - 1] or p[idx2 - 1] == '?':
            dp[idx1][idx2] = self.solve(idx1 - 1, idx2 - 1, s, p, dp)
            return dp[idx1][idx2]
        elif p[idx2 - 1] == '*':
            dp[idx1][idx2] = self.solve(idx1 - 1, idx2, s, p, dp) or self.solve(idx1, idx2 - 1, s, p, dp)
            return dp[idx1][idx2]
        else:
            dp[idx1][idx2] = False
            return dp[idx1][idx2]

    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return self.solve(m, n, s, p, dp)
    

# Tabulation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]

        # base case 1
        dp[0][0] = True

        # base case 2
        for idx1 in range(1, m+1):
            dp[idx1][0] = False

        # base case 3
        for idx2 in range(1, n+1):
            dp[0][idx2] = dp[0][idx2 - 1] and p[idx2 - 1] == '*'

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if s[idx1 - 1] == p[idx2 - 1] or p[idx2 - 1] == '?':
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
                elif p[idx2 - 1] == '*':
                    dp[idx1][idx2] = dp[idx1 - 1][idx2] or dp[idx1][idx2 - 1]
                else:
                    dp[idx1][idx2] = False
        
        return dp[m][n]
    

# Tabulation (Space-Optimised)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False for _ in range(n+1)]
        curr = [False for _ in range(n+1)]
        
        # base case 1
        prev[0] = True

        # base case 2 automatically handled as dp is initialized as False

        # base case 3
        for idx2 in range(1, n+1):
            prev[idx2] = prev[idx2 - 1] and p[idx2 - 1] == '*'

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if s[idx1 - 1] == p[idx2 - 1] or p[idx2 - 1] == '?':
                    curr[idx2] = prev[idx2 - 1]
                elif p[idx2 - 1] == '*':
                    curr[idx2] = prev[idx2] or curr[idx2 - 1]
                else:
                    curr[idx2] = False
            prev = curr[:]
        
        return prev[n]