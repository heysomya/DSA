# Brute Force
class Solution:
    def solve(self, row, col, matrix, n):
        if row == 0:
            return matrix[0][col]

        up, dleft, dright = float('inf'), float('inf'), float('inf')
        if row>0: up = self.solve(row-1, col, matrix, n)
        if col>0: dleft = self.solve(row-1, col-1, matrix, n)
        if col<n-1: dright = self.solve(row-1, col+1, matrix, n)

        return matrix[row][col] + min(up, dleft, dright)


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        mini = float('inf')
        for col in range(n):
            mini = min(mini, self.solve(n-1, col, matrix, n))

        return mini


# Memoization
class Solution:
    def solve(self, row, col, matrix, n, dp):
        if row == 0:
            return matrix[0][col]
        
        if dp[row][col] != None: return dp[row][col]

        up, dleft, dright = float('inf'), float('inf'), float('inf')
        if row>0: up = self.solve(row-1, col, matrix, n, dp)
        if col>0: dleft = self.solve(row-1, col-1, matrix, n, dp)
        if col<n-1: dright = self.solve(row-1, col+1, matrix, n, dp)

        dp[row][col] = matrix[row][col] + min(up, dleft, dright)

        return dp[row][col]


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[None for _ in range(n)] for _ in range(n)]

        mini = float('inf')
        for col in range(n):
            mini = min(mini, self.solve(n-1, col, matrix, n, dp))
            dp[n-1][col] = mini

        return mini


# Tabulation
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for col in range(n):
            dp[0][col] = matrix[0][col]

        for row in range(1, n):
            for col in range(n):
                up, dleft, dright = float('inf'), float('inf'), float('inf')
                if row>0: up = dp[row-1][col]
                if col>0: dleft = dp[row-1][col-1]
                if col<n-1: dright = dp[row-1][col+1]
                dp[row][col] = matrix[row][col] + min(up, dleft, dright)

        return min(dp[n-1])


# Tabulation - O(2N) space
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = [0 for _ in range(n)]
        curr = [0 for _ in range(n)]

        for col in range(n):
            prev[col] = matrix[0][col]

        for row in range(1, n):
            for col in range(n):
                up, dleft, dright = float('inf'), float('inf'), float('inf')
                if row>0: up = prev[col]
                if col>0: dleft = prev[col-1]
                if col<n-1: dright = prev[col+1]
                curr[col] = matrix[row][col] + min(up, dleft, dright)
            prev = curr[:]

        return min(prev)