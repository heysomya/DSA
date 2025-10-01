# Brute Force
class Solution:
    def solve(self, idx1, idx2, word1, word2):
        # base case
        if idx1 == 0 and idx2 == 0:
            return 0

        if idx2 ==  0:
            return idx1

        if idx1 == 0:
            return idx2 

        
        if word1[idx1 - 1] == word2[idx2 - 1]:
            return self.solve(idx1 - 1, idx2 - 1, word1, word2)
        else:
            insert = self.solve(idx1, idx2 - 1, word1, word2)
            delete = self.solve(idx1 - 1, idx2, word1, word2)
            replace = self.solve(idx1 - 1, idx2 - 1, word1, word2)

            return 1 + min(insert, delete, replace)


    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        return self.solve(m, n, word1, word2)
    

# Memoization
class Solution:
    def solve(self, idx1, idx2, word1, word2, dp):
        # base case
        if idx1 == 0 and idx2 == 0:
            return 0

        if idx2 == 0:
            return idx1

        if idx1 == 0:
            return idx2 

        if dp[idx1][idx2] != -1:
            return dp[idx1][idx2]
        
        if word1[idx1 - 1] == word2[idx2 - 1]:
            dp[idx1][idx2] = self.solve(idx1 - 1, idx2 - 1, word1, word2, dp)
            return dp[idx1][idx2]
        else:
            insert = self.solve(idx1, idx2 - 1, word1, word2, dp)
            delete = self.solve(idx1 - 1, idx2, word1, word2, dp)
            replace = self.solve(idx1 - 1, idx2 - 1, word1, word2, dp)

            dp[idx1][idx2] = 1 + min(insert, delete, replace)
            return dp[idx1][idx2]


    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        return self.solve(m, n, word1, word2, dp)
    

# Tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for idx1 in range(1, m+1):
            dp[idx1][0] = idx1
        
        for idx2 in range(1, n+1):
            dp[0][idx2] = idx2

        for idx1 in range(1, m+1):
            for idx2 in range(1, n+1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
                else:
                    insert = dp[idx1][idx2 - 1]
                    delete = dp[idx1 - 1][idx2]
                    replace = dp[idx1 - 1][idx2 - 1]

                    dp[idx1][idx2] = 1 + min(insert, delete, replace)

        return dp[m][n]
    

# Tabulation (Space Optimised)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        prev = [0 for _ in range(n+1)] 
        curr = [0 for _ in range(n+1)] 
        
        for idx2 in range(1, n+1):
            prev[idx2] = idx2

        for idx1 in range(1, m+1):
            curr[0] = idx1
            for idx2 in range(1, n+1):
                if word1[idx1 - 1] == word2[idx2 - 1]:
                    curr[idx2] = prev[idx2 - 1]
                else:
                    insert = curr[idx2 - 1]
                    delete = prev[idx2]
                    replace = prev[idx2 - 1]

                    curr[idx2] = 1 + min(insert, delete, replace)
            prev = curr[:]

        return prev[n]