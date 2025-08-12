# Brute Force - Recursive
class Solution:
    def f(self, n):
        if n<=2:
            return n

        return self.f(n-1) + self.f(n-2) 

    def climbStairs(self, n: int) -> int:
        return self.f(n)


# Better - Memoized
class Solution:
    def f(self, n, dp):
        if n<=2:
            return n

        if dp[n] != -1: return dp[n]

        dp[n] = self.f(n-1, dp) + self.f(n-2, dp) 
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.f(n, dp)


# Better - Tabulation, Linear Space
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n
        dp = [0] * (n+1)

        dp[1] = 1
        dp[2] = 2

        i = 3
        while i<=n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1

        return dp[n]