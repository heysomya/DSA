# Brute Force
class Solution:
    def solve(self, m, n):
        if m<0 or n<0: return 0

        if m==0 and n==0: return 1

        up, left = 0, 0
        if m>0: up = self.solve(m-1, n)
        if n>0: left = self.solve(m, n-1)

        return up + left

    def uniquePaths(self, m: int, n: int) -> int:
        return self.solve(m-1, n-1)


# Memoization
class Solution2:
    def solve(self, m, n, dp):
        if m<0 or n<0: return 0
        if m==0 and n==0: return 1

        if dp[m][n] != -1: return dp[m][n]

        up, left = 0, 0
        if m>0: up = self.solve(m-1, n, dp)
        if n>0: left = self.solve(m, n-1, dp)

        dp[m][n] = up + left
        return dp[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(m-1, n-1, dp)


# Tabulation
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0: dp[i][j] = 1
                else:
                    up, left = 0, 0
                    if i>0: up = dp[i-1][j]
                    if j>0: left = dp[i][j-1]
                    dp[i][j] = up + left

        return dp[-1][-1]


# Tabulation - No extra space
class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0 for _ in range(n)]

        for i in range(m):
            curr = [0 for _ in range(n)]
            for j in range(n):
                if i==0 and j==0: curr[j] = 1
                else:
                    up, left = 0, 0
                    if i>0: up = prev[j]
                    if j>0: left = curr[j-1]
                    curr[j] = up + left
            prev = curr

        return prev[-1]


def main():
    inputArr = [(3, 7), (3, 2)]

    for (m, n) in inputArr:
        s = Solution4()
        res = s.uniquePaths(m, n)
        print(res)

main()