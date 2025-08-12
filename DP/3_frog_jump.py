# Brute Force - Recursive
class Solution:
    def f(self, heights, n, i):

        if i==n-1:
            return 0

        if i==n-2:
            return abs(heights[n-1] - heights[n-2]) 
        
        dist1 = abs(heights[i+1] - heights[i]) + self.f(heights, n, i+1)
        dist2 = abs(heights[i+2] - heights[i]) + self.f(heights, n, i+2)

        return min(dist1, dist2)

    def frogJump(self, heights):
        n = len(heights)
        return self.f(heights, n, 0)


# Better - Memoization
class Solution2:
    def f(self, heights, dp, n, i):
        if i==n-1:
            return 0

        if i==n-2:
            return abs(heights[n-1] - heights[n-2])
        
        if dp[i] != -1: return dp[i]
        
        dist1 = abs(heights[i+1] - heights[i]) + self.f(heights, dp, n, i+1)
        dist2 = abs(heights[i+2] - heights[i]) + self.f(heights, dp, n, i+2)

        dp[i] = min(dist1, dist2)
        return dp[i] 

    def frogJump(self, heights):
        n = len(heights)
        dp = [-1] * (n+1)
        return self.f(heights, dp, n, 0)


# Better - Tablulation, Linear Space 
class Solution3:
    def frogJump(self, heights):
        n = len(heights)
        dp = [0] * (n+1)
        dp[n-2] =  abs(heights[n-1] - heights[n-2])
        
        i = n-3
        while i >= 0:
            dist1 = dp[i+1] + abs(heights[i+1] - heights[i])
            dist2 = dp[i+2] + abs(heights[i+2] - heights[i])
            dp[i] = min(dist1, dist2)
            i-=1
            
        return dp[0]


def main():
    s = Solution3()
    # heights = [2, 1, 3, 5, 4]
    # 2
    heights = [7, 5, 1, 2, 6]
    # 9
    res = s.frogJump(heights)
    print(res)

main()