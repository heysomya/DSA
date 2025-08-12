# Brute Force - Recursive
class Solution:
    def f(self, n):
        if n==0 or n==1:
            return n

        return self.f(n-1) + self.f(n-2)

    def fib(self, n: int) -> int:
        return self.f(n)


# Better - Memoized DP 
class Solution:
    def f(self, dp, n):
        if n==0 or n==1:
            return n

        if dp[n] != -1:
            return dp[n]

        dp[n] = self.f(dp, n-1) + self.f(dp, n-2) 
        return dp[n]

    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.f(dp, n)


# Better - Tabulation but linear space
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1: return n
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1

        i = 2
        while i<=n:
            dp[i] = dp[i-1] + dp[i-2]
            i+=1
            
        return dp[n]


# Optimal - Tabulation and Constant Space
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1: return n
        prev2 = 0
        prev = 1

        i = 2
        while i<=n:
            curr = prev + prev2 
            prev2 = prev
            prev = curr
            i+=1

        return prev 