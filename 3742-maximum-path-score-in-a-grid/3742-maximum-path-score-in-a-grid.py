class Solution(object):
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                for cost in range(k + 1):
                    if dp[i][j][cost] == -1:
                        continue
                    
                    # Down
                    if i + 1 < m:
                        val = grid[i + 1][j]
                        new_cost = cost + (val > 0)
                        if new_cost <= k:
                            dp[i + 1][j][new_cost] = max(
                                dp[i + 1][j][new_cost],
                                dp[i][j][cost] + val
                            )
                    
                    # Right
                    if j + 1 < n:
                        val = grid[i][j + 1]
                        new_cost = cost + (val > 0)
                        if new_cost <= k:
                            dp[i][j + 1][new_cost] = max(
                                dp[i][j + 1][new_cost],
                                dp[i][j][cost] + val
                            )
        
        ans = max(dp[m - 1][n - 1])
        return ans if ans != -1 else -1