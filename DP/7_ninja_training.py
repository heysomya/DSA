from typing import *

# Brute Force
# def solve(points, idx, prev_chosen):
#     if idx==-1:
#         return 0

#     maxi = -1
#     for j in range(3):
#         if j!= prev_chosen:
#             pick = points[idx][j] + solve(points, idx - 1, j)
#             maxi = max(maxi, pick)
    
#     return maxi
  
# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     # Write your code here.
#     n = len(points)

#     return solve(points, n-1, -1)


# Memoization
# def solve(points, idx, prev_chosen, dp):
#     if idx==-1:
#         return 0

#     if dp[idx][prev_chosen] != -1:
#         return dp[idx][prev_chosen]

#     maxi = -1
#     for j in range(3):
#         if j != prev_chosen:
#             pick = points[idx][j] + solve(points, idx - 1, j, dp)
#             maxi = max(maxi, pick)
    
#     dp[idx][prev_chosen] = maxi
#     return dp[idx][prev_chosen]
  
# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     # Write your code here.
#     n = len(points)

#     dp = [[-1 for _ in range(4)] for _ in range(n)]

#     return solve(points, n-1, 3, dp)


# Tabulation
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    # Write your code here.
    n = len(points)

    dp = [[-1 for _ in range(4)] for _ in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            maxi = -1
            for task in range(3):
                if task != last:
                    pick = points[day][task] + dp[day-1][task]
                    maxi = max(maxi, pick)
            dp[day][last] = maxi

    return dp[n-1][3]

def main():
    n = 3
    points =  [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
    res = ninjaTraining(n, points)
    print(res)

main()
