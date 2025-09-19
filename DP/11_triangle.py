from typing import List

# Brute Force
class Solution:
    def solve(self, row, col, triangle, n):
        if row == n-1:
            return triangle[row][col]

        down = self.solve(row + 1, col, triangle, n)
        diag = self.solve(row + 1, col + 1, triangle, n)
        
        return triangle[row][col] + min(down, diag)


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        return self.solve(0, 0, triangle, n)


# Memoization
class Solution:
    def solve(self, row, col, triangle, n, dp):
        if row == n-1:
            return triangle[row][col]

        if dp[row][col] != None: return dp[row][col]

        down = self.solve(row + 1, col, triangle, n, dp)
        diag = self.solve(row + 1, col + 1, triangle, n, dp)
        
        dp[row][col] = triangle[row][col] + min(down, diag)
        return dp[row][col]


    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None for _ in range(n)] for _ in range(n)]
        return self.solve(0, 0, triangle, n, dp)


# Tabulation
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None for _ in range(n)] for _ in range(n)]

        # base case
        for col in range(n):
            dp[n-1][col] = triangle[n-1][col]
    
        for row in range(n-2, -1, -1):
            for col in range(row+1):
                down = dp[row + 1][col]
                diag = dp[row + 1][col + 1]
                dp[row][col] = triangle[row][col] + min(down, diag)

        return dp[0][0]


# Tabulation - O(2N) space
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        prev = [None for _ in range(n)]
        curr = [None for _ in range(n)]

        # base case
        for col in range(n):
            prev[col] = triangle[n-1][col]

        for row in range(n-2, -1, -1):
            for col in range(row+1):
                down = prev[col]
                diag = prev[col + 1]
                curr[col] = triangle[row][col] + min(down, diag)

            prev = curr[:]

        return prev[0]