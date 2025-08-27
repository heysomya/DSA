# Brute Force
class Solution:
    def solve(self, row, col1, col2, grid, m, n):
        # base case
        if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n: return float('-inf')

        if row == m-1:
            if col1 == col2: return grid[row][col1]
            else: return grid[row][col1] + grid[row][col2]
        
        dirs = [-1, 0, 1]
        maxi = float('-inf')
        for dir1 in dirs:
            for dir2 in dirs:
                ncol1, ncol2 = col1 + dir1, col2 + dir2
                maxi = max(maxi, self.solve(row+1, ncol1, ncol2, grid, m, n))
        
        if col1 == col2:
            return grid[row][col1] + maxi
        
        return grid[row][col1] + grid[row][col2] + maxi


    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        return self.solve(0, 0, n-1, grid, m, n)


# Memoization
class Solution:
    def solve(self, row, col1, col2, grid, m, n, dp):
        # base case
        if col1 < 0 or col1 >= n or col2 < 0 or col2 >= n: return float('-inf')

        if row == m-1:
            if col1 == col2: return grid[row][col1]
            else: return grid[row][col1] + grid[row][col2]

        if dp[row][col1][col2] != -1: return dp[row][col1][col2]
        
        dirs = [-1, 0, 1]
        maxi = float('-inf')
        for dir1 in dirs:
            for dir2 in dirs:
                ncol1, ncol2 = col1 + dir1, col2 + dir2
                maxi = max(maxi, self.solve(row+1, ncol1, ncol2, grid, m, n, dp))
        
        if col1 == col2:
            dp[row][col1][col2] = grid[row][col1] + maxi
            return dp[row][col1][col2]
        
        dp[row][col1][col2] = grid[row][col1] + grid[row][col2] + maxi
        return dp[row][col1][col2]


    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        
        return self.solve(0, 0, n-1, grid, m, n, dp)


# Tabulation
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]

        # base case
        for col1 in range(n):
            for col2 in range(n):
                if col1 == col2: dp[m-1][col1][col2] = grid[m-1][col1]
                else: dp[m-1][col1][col2] = grid[m-1][col1] + grid[m-1][col2]

        dirs = [-1, 0, 1]
        for row in range(m-2, -1, -1):
            for col1 in range(n):
                for col2 in range(n):
                    maxi = float('-inf')
                    for dir1 in dirs:
                        for dir2 in dirs:
                            ncol1, ncol2 = col1 + dir1, col2 + dir2
                            if 0<=ncol1<n and 0<=ncol2<n:
                                maxi = max(maxi, dp[row+1][ncol1][ncol2])

                    if col1 == col2:
                        dp[row][col1][col2] = grid[row][col1] + maxi
                    else:
                        dp[row][col1][col2] = grid[row][col1] + grid[row][col2] + maxi

        
        return dp[0][0][n-1]


# Tabulation - Reduced space to 2D
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        prev = [[0 for _ in range(n)] for _ in range(n)]

        # base case
        for col1 in range(n):
            for col2 in range(n):
                if col1 == col2: prev[col1][col2] = grid[m-1][col1]
                else: prev[col1][col2] = grid[m-1][col1] + grid[m-1][col2]

        dirs = [-1, 0, 1]
        for row in range(m-2, -1, -1):
            curr = [[0 for _ in range(n)] for _ in range(n)]
            for col1 in range(n):
                for col2 in range(n):
                    maxi = float('-inf')
                    for dir1 in dirs:
                        for dir2 in dirs:
                            ncol1, ncol2 = col1 + dir1, col2 + dir2
                            if 0<=ncol1<n and 0<=ncol2<n:
                                maxi = max(maxi, prev[ncol1][ncol2])

                    if col1 == col2:
                        curr[col1][col2] = grid[row][col1] + maxi
                    else:
                        curr[col1][col2] = grid[row][col1] + grid[row][col2] + maxi
            prev = curr

        
        return prev[0][n-1]