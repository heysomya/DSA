# Brute Force - Recursion
class Solution:
    def f(self, heights, n, k, i):
        if i==n-1:
            return 0

        min_dist = float('inf')
        for j in range(1, k+1):
            if (i+j) < n:
                dist = abs(heights[i+j] - heights[i]) + self.f(heights, n, k, i+j)
                min_dist = min(min_dist, dist)
            else:
                break

        return min_dist

    def frogJump(self, heights, k):
        n = len(heights)
        return self.f(heights, n, k, 0)


# Better - Memoization
class Solution2:
    def f(self, heights, dp, n, k, i):
        if i==n-1:
            return 0

        if dp[i] != -1: return dp[i]

        min_dist = float('inf')
        for j in range(1, k+1):
            if (i+j) < n:
                dist = abs(heights[i+j] - heights[i]) + self.f(heights, dp, n, k, i+j)
                min_dist = min(min_dist, dist)
            else:
                break

        dp[i] = min_dist
        return dp[i]

    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1] * (n+1)
        return self.f(heights, dp, n, k, 0)


# Optimal - Tabulation
class Solution3:
    def frogJump(self, heights, k):
        n = len(heights)
        dp = [0] * (n+1)
        
        for i in range(n-2, -1, -1):
            min_dist = float('inf')
            for j in range(1, k+1):
                if i+j < n:
                    dist = abs(heights[i+j] - heights[i]) + dp[i+j]
                    min_dist = min(min_dist, dist)
                else:
                    break
            dp[i] = min_dist


        return dp[0]



def main():
    heightsArr = [[[10, 5, 20, 0, 15], 2], [[15, 4, 1, 14, 15], 3]]

    for [heights, k]  in heightsArr:
        s = Solution3()
        res = s.frogJump(heights, k)
        print(res)

main()