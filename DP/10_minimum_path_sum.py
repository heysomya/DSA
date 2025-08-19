# Brute Force
class Solution:
    def solve(self, grid, m, n):
        if m<0 or n<0: return float('inf')

        if m==0 and n==0: return grid[0][0]

        up = self.solve(grid, m-1, n)
        left = self.solve(grid, m, n-1)
        mini = min(up, left)

        return grid[m][n] + mini

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        return self.solve(grid, m-1, n-1)


# Memoization
class Solution2:
    def solve(self, grid, m, n, dp):
        if m<0 or n<0: return float('inf')

        if m==0 and n==0: return grid[0][0]

        if dp[m][n] != -1: return dp[m][n]

        up = self.solve(grid, m-1, n, dp)
        left = self.solve(grid, m, n-1, dp)
        dp[m][n] = grid[m][n] + min(up, left)

        return dp[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solve(grid, m-1, n-1, dp)


# Tabulation
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0: continue
                else:
                    up, left = float('inf'), float('inf')
                    if i>0: up = dp[i-1][j]
                    if j>0: left = dp[i][j-1]
                    dp[i][j] = grid[i][j] + min(up, left)

        return dp[-1][-1]


# Tabulation - O(n) extra space
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [0 for _ in range(n)]

        for i in range(m):
            curr = [0 for _ in range(n)]
            for j in range(n):
                if i==0 and j==0: curr[j] = grid[i][j]
                else:
                    up, left = float('inf'), float('inf')
                    if i>0: up = prev[j]
                    if j>0: left = curr[j-1]
                    curr[j] = grid[i][j] + min(up, left)

            prev = curr

        return prev[-1]