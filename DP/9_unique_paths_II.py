# Brute Force
class Solution:
    def solve(self, grid, m, n):
        if m<0 or n<0: return 0

        if grid[m][n] == 1: return 0

        if m==0 and n==0:
            return 1

        up = self.solve(grid, m-1, n)
        left = self.solve(grid, m, n-1)

        return up + left

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.solve(grid, m-1, n-1)


# Memoization
class Solution2:
    def solve(self, grid, m, n, dp):
        if m<0 or n<0: return 0

        if grid[m][n] == 1: return 0

        if dp[m][n] != -1: return dp[m][n]

        up = self.solve(grid, m-1, n, dp)
        left = self.solve(grid, m, n-1, dp)

        dp[m][n] = up + left

        return dp[m][n]

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        return self.solve(grid, m-1, n-1, dp)


# Tabulation
class Solution3:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0: dp[0][0] = 1
                elif grid[i][j] == 1: dp[i][j] = 0
                else:
                    up, left = 0, 0
                    if i>0: up = dp[i-1][j]
                    if j>0: left = dp[i][j-1]
                    dp[i][j] = up + left
        
        return dp[-1][-1]


# Tabulation - No extra space
class Solution4:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return 0

        m, n = len(grid), len(grid[0])
        prev = [0 for _ in range(n)]

        for i in range(m):
            curr = [0 for _ in range(n)]
            for j in range(n):
                if i==0 and j==0: curr[0] = 1
                elif grid[i][j] == 1: curr[j] = 0
                else:
                    up, left = 0, 0
                    if i>0: up = prev[j]
                    if j>0: left = curr[j-1]
                    curr[j] = up + left
            prev = curr
        
        return prev[-1]


